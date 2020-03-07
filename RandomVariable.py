# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 04:03:56 2019

Write a code that generates U(0,1) using a built in function and transform the
 first n generated
numbers into: (n is an input from the user)
a) Uniform (-5, 100)
b) Exponential with mean equals 100.

@author: Seham Nasr
"""

import numpy 
import math
import random 
import matplotlib.pyplot as plt

print ('\n ______________Generated Random variable ___________\n   ')
n=input('please enter N:')
n=int(n)
value=numpy.random.uniform(0,1,n)
#print ('\n     u(0,1) :   ',value)
#plt.title("Uniform distribution")
#plt.plot(value)
#plt.xlabel("Value")
#plt.ylabel("frequency")
#plt.show()
##rv=numpy.random.uniform(-5,100,n)
#[min,max]=[-5,100]
#print ("This is uniform function way 1: (x-a)/(b-a)")
#un=(value-min)/(max-min)
#print("uniform dist.  ",un)
#plt.title("Standard Uniform distribution (CDF)")
#plt.plot(value,un)
#plt.xlabel("x")
#plt.ylabel("F(x)")
#plt.show()
##
#print ("\nThis is uniform, mapping way 2:")
#value2=numpy.random.uniform(-5,100,n)
#rv = value*(max-min) + min
#print('uniform(',min,',',max,'): ',rv,sep='')
#plt.title("Uniform distribution")
#plt.plot(value2,rv)
#plt.xlabel("value")
#plt.ylabel("frequency")
#plt.show()

#b-Exponential with mean = 100



print('\nExponential with mean =100 is :  ')
y=[]
z=-(numpy.log(1-value))/100
for u in value:
    x = -(math.log(1-u))/100
    y.append(x)
y.sort()
plt.plot(y)
#plt.hist(z)
#plt.plot(bins, numpy.ones_like(bins), linewidth=5, color='r')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("The percent point function (ppf) is the inverse of the cdf")
plt.show()
    
  

   
    
