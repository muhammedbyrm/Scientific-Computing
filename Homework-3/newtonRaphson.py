# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 20:35:53 2022

@author: muham
"""

from sympy import *
import numpy as np
import matplotlib.pyplot as plt




def newtonRaphson(f,x0,numIter):
    
    xValues = []
    yValues = []
  
    Df = f.diff(x)
    

    #print('xn iter ',1, " ", x0)
    for n in range(numIter+1):
        
        
        f_xn = f.subs(x,x0)                  
        Df_xn = Df.subs(x,x0)

        if Df_xn == 0:
            print("No solution found.")
            return None
        x0 = (float)(x0 - f_xn/Df_xn)
        
        
        if(n>4): # this line is just for ploting
            xValues.append(n)
            yValues.append(x0)


    print("The final value of root in " , numIter ," iterations is ", x0)   

    plt.plot(xValues, yValues)
    plt.xlabel('x - values')
    plt.ylabel('r o o t s')   
    plt.show()


x = Symbol('x')
f1 = x**3 - x - 1  #first function
f2 = x**2 - (5**0.5)*x #second function

f1_initial = 1
f2_initial = 2


numIter = 20

newtonRaphson(f1,f1_initial,numIter)
newtonRaphson(f2,f2_initial,numIter)

