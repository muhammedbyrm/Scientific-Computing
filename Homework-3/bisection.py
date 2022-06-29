# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:30:21 2022

@author: muham
"""
import matplotlib.pyplot as plt

def bisection(f, a, b, iterNum):
    
    xValues = []
    yValues = []
    
    if(f(a)*f(b) > 0):
        print("There is no root")
        return

    for i in range(iterNum+1):
        midPoint = (a + b ) / 2.0
        #print("x values: ", i, " root values: ", midPoint)
        
         
        if(i>9): # in order print x values between 10 and 50, this part is just for ploting
            xValues.append(i)
            yValues.append(midPoint)
        
        if(f(a)*f(midPoint) < 0):
            b = midPoint
        elif(f(b)*f(midPoint) < 0):
            a = midPoint
        elif midPoint == 0:
            print("Found exact solution.")
            return midPoint
    
    
    print("The final value of root in " , iterNum ," iterations is ", midPoint)
    
    plt.plot(xValues, yValues)
    plt.xlabel('x - values')
    plt.ylabel('r o o t s')   
    plt.show()
     
    
    return (a+b)/2



f1_a = 3
f1_b = 4

f2_a=-4
f2_b=-3

f1 = lambda x: 0.5*(x) - pow((x+1),(1/3))
f2 = lambda x: pow(x,3) + 5* pow(x,2) + 7*x + 5

iterNum = 50

bisection(f1,f1_a,f1_b,iterNum)
print("******************************************")
bisection(f2,f2_a,f2_b,iterNum)