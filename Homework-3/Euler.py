# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:40:19 2022

@author: muham
"""

# Python program to implement Euler method for sample differential equation "dy / dx = y-x"

def dydx(x,y):
    return y-x

def myEuler(x0, y, x, h):
 
    while x0 < x:
        y = y + h * dydx(x0,y)
        x0 = x0 +h
        #print("Approximate solution at x = ", x0, " is ", "%.6f"% y)
    print("Result is" , "%.6f"% y)
                
x0 = 0
y = 0
x = 20
h = 0.1
myEuler(x0, y, x, h)