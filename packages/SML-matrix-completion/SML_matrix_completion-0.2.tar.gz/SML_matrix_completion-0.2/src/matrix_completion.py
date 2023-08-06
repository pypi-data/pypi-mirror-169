import math
import numpy as np
import random  as rd
import matplotlib.pyplot as plt
from matplotlib import colors
import numba
from numba import njit
import time
from matplotlib.pyplot import figure

from numba.typed import List
from collections import defaultdict
import random as rd

from scipy.sparse import csr_matrix
from scipy import linalg

import time


def _help():
    text = "This program computes minimum norm of a vector that satisfies some conditons.\n"
    text += "res = mc.complete( A, b, z, n1, n2,  mu, beta, loop_size ).\n"
    print(text)

def proximal_nuclear(Y, n1, n2, mu, beta ):
    tau = (mu/beta)
    U,Sigma,V = linalg.svd(np.reshape(Y, (n1, n2)))
    full_sigma  = np.zeros( (n1,n2), np.float_)
    for i in range(len(Sigma)):
        if Sigma[i]>tau:
            full_sigma[i][i] = Sigma[i]-tau
    return (U@full_sigma)@V
# proximal_nuclear(yticks, beta, mu )


def compute_x(z, A_TA, A_Tb, n1, n2, mu, beta):
    y = z-(1/beta)*( A_TA@z- A_Tb )
    return proximal_nuclear(y , n1, n2, mu, beta).flatten()

def vec_to_mat_X(X):
    return np.reshape(X, (n1, n2))
# vec_to_mat_X(X).flatten()-X

def main_loop(A_TA, A_Tb, z, n1, n2, mu, beta, loop_size ):
    t=np.zeros( (loop_size), np.float_)
    t[0]=1
    Z=z
    Xold = compute_x(Z, A_TA, A_Tb, n1, n2, mu, beta)
    # print(Xold.shape)
    # z=np.zeros( (loop_size), np.float_)
    for n in range(loop_size-1):

        t[n+1]= (math.sqrt(4*t[n]*t[n]+1)+1)/2
        lambda_loop = 1+ (t[n]-1)/t[n+1]


        X = compute_x(Z, A_TA, A_Tb, n1, n2, mu, beta)

        Z= Xold+ lambda_loop*(X-Xold)
        # print(Z)

        # print(Z)
        Xold = X

    # print(np.linalg.norm(vec_to_mat_X(Z)-M)/ np.linalg.norm(M))
    return Z
#
# M_fake = main_loop(z, beta=1, mu=0.01, loop_size=1000 )


def complete( A, b, z, n1, n2,  mu, beta, loop_size ):
    A_T=  A.T
    A_TA =A_T@A
    A_Tb  =  A_T@b

    return main_loop(A_TA, A_Tb, z, n1, n2, mu,  beta, loop_size )
