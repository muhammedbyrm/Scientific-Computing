# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 16:38:27 2022

@author: muham
"""
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt


def myInterpolationFunc(xData, yData, interpolationPoint):
    n = np.shape(yData)[0]
    coeff_vector = np.zeros([n, n]) 
    coeff_vector[::, 0] = yData     

    for k in range(len(xData)):
        if (xData[k] == interpolationPoint):
            print("interpolationPoint is already calculated")
            return yData[k]

    for j in range(1, n):
        for i in range(n - j):
            if (xData[i + j] - xData[i]) == 0:
                coeff_vector[i][j] = 0
                continue
            coeff_vector[i][j] = (coeff_vector[i + 1][j - 1] - coeff_vector[i][j - 1]) / (xData[i + j] - xData[i])

    coeff_vector = coeff_vector[0]
    return result(coeff_vector, interpolationPoint, xData)


def compr(dict,interpolationPoint):
    
    x = []
    y = []
    
    for key in dict :
        x.append(key)
        y.append(dict[key])
        
    x = list(map(float, x))
    y = list(map(float, y))
     
    
    f = interp1d(x, y, kind='cubic')
    print("interp1d result is: " , f(interpolationPoint))
    

#this function draw a graph from x and y values of data1.txt
def plot():
    xTarget = []
    yTarget = []
    
    with open("data1.txt") as fobj:
        for line in fobj:
            row = line.split()
            xTarget.append(row[0])
            yTarget.append(row[-1]) 

    xTarget = np.array(xTarget)
    yTarget = list(map(int, yTarget))
    
    plt.plot(xTarget, yTarget)
    plt.plot(xTarget, yTarget,'o')
 

    plt.xlabel('x - values')
    plt.ylabel('y - values')

    plt.show()
    
   

# this fuction read data from txt files and calculate and return x and y values that interpolationPoint is between them
# for instance for point 20.2 it will return 19.6 20.2 20.3 20.3 as x values and corresponding y values which are 30.6 30.2 28.6 28.6
def readFile(fileName, interpolationPoint):
    
    xTarget = []
    yTarget = []
    
    with open(fileName) as fobj:
        for line in fobj:
            row = line.split()
            xTarget.append(row[0])
            yTarget.append(row[-1])
          
    xTarget = np.array(xTarget)
    yTarget = np.array(yTarget)

    dict = {}

    for j in range(len(xTarget)):
        key = (float)(xTarget[j])
        if key in dict:
            continue
        else:
            dict[(float)(xTarget[j])] = yTarget[j]
    
    compr(dict,interpolationPoint)
    
    small_x_values = []
    big_x_values = []

    for i in range(len(xTarget)):
        if (float)(xTarget[i]) <= interpolationPoint:
            small_x_values.append(xTarget[i])
        else:
            big_x_values.append(xTarget[i])

    small_x_values = np.array(small_x_values) 
    big_x_values = np.array(big_x_values)

    xData = np.zeros(4)  # x values that i will use, I use 4 point to get equation 

    if (len(small_x_values) == 1):
        xData[0] = (float)(small_x_values[len(small_x_values) - 1])
        xData[1] = big_x_values[0]
        xData[2] = big_x_values[1]
        xData[3] = big_x_values[2]
    elif (len(big_x_values) == 1):
        xData[0] = (float)(small_x_values[len(small_x_values) - 3])
        xData[1] = small_x_values[len(small_x_values) - 2]
        xData[2] = small_x_values[len(small_x_values) - 1]
        xData[3] = big_x_values[0]
    else:
        xData[0] = (float)(small_x_values[len(small_x_values) - 2])
        xData[1] = small_x_values[len(small_x_values) - 1]
        xData[2] = big_x_values[0]
        xData[3] = big_x_values[1]

    yData = np.zeros(4)
    for i in range(len(xData)):
        key = xData[i]
        yData[i] = dict[key]
    return xData, yData



def result(coeff_vector, point, xData):
    result = coeff_vector[0] + coeff_vector[1] * (point - xData[0]) + coeff_vector[2] * (point - xData[0]) * (
                point - xData[1]) + coeff_vector[3] * (point - xData[0]) * (point - xData[1]) * (
                         point - xData[2])
    return result


fileName = "data4.txt" 
interpolationPoint = -0.51
xData, yData = readFile(fileName, interpolationPoint)
result = myInterpolationFunc(xData, yData, interpolationPoint)
print("My result is", result)
plot()

