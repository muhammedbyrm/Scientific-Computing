# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 18:58:44 2021

@author: muhammed bayram 17050111018
"""

import numpy as np
import copy
import scipy
import scipy.linalg as linalg
import scipy.io as input



def jakobi(A, b, numberOfIteration):
    dimension = len(A)
    x = [0] * dimension
    p = [0] * dimension
    sum = 0.0

    for i in range(numberOfIteration):
        for k in range(dimension):
            for j in range(dimension):
                if j == k or A[k, k] == 0 :
                    continue
                else:
                    sum += (A[k, j] * p[j])
            x[k] = (b[k] - sum) / A[k, k]
            sum = 0
        p = copy.copy(x)
    return p


if __name__ == '__main__':
    arr = input.mmread("Trefethen_20.mtx")
    dimension = arr.shape[0]
    arr = arr + np.transpose(arr) + np.identity(dimension)     
    b = [1] * dimension
    numberOfIteration = 30

    myS= np.array(jakobi(arr, b, numberOfIteration))  
    exact = scipy.linalg.solve(arr, b)
    #print("my result", myS)
    #print("exacccct", exact)
    print(np.linalg.norm((myS -exact), ord = 1))
 
    
    
    
    