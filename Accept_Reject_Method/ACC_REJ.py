# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 00:19:05 2019

@author: Seham Nasr
"""
"""
Accept-Reject Method:
Write a code that generates a normal distribution and draw 
plots for each of the following three cases.
a) Normal (0, 1).
b) Normal (100, 1).
c) Normal with mean 100 and variance 100.
Note: the p.d.f of a normal r.v. with 0 mean and variance 1 is:
    f X(t)= 2*e^(−t2/2)/√2π  , 0<t<∞

"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


import pylab

from scipy.stats import norm

print('\n -------- Accept-Reject method for Generating Random Variable--------------\n')

#generate Random variable Y
def generateY():
    Y=np.random.uniform(0,1)
    return(-np.log(Y))
    
#generate Uniform Random variable
def generatingU():
    u=np.random.uniform(0,1)
    return u

#this is the target function f(x) for normal distribution
f =lambda x: ((2* np.exp(-(x**2/2)) ) / np.sqrt(2*np.pi))

#calculate the integration for the function f "area under the curve
quad(f,-np.inf,np.inf)    

#This is for graph purpose     
range1 = np.arange(-3.0,3.0,0.01)

#The invertible function I used here the exponential function g(x)=e^-x
g =lambda x: np.exp(-x)

#this is for graph purpose    
range2=np.arange(0.0,3.0,0.01)
#-------Here you can uncomment to see the graphs before applying the method
#plt.plot(range1,f(range1))
#plt.plot(range2,g(range2))
#plt.plot(-range2,g(range2))
range3=np.arange(50.0,100.0,.01)

C=1.32    # this is the max constant which used to multiply with g(x) func
#plt.subplot(111)
#plt.plot(range1,f(range1))
#plt.plot(range2,C* g(range2))
#plt.plot(-range2,C* g(range2))

fx=[]
fx1=[]
fx2=[]
#start the loop for generating r.v using accept-reject method
for i in range(100):
    while(1):
        x=generateY()
        u=generatingU()
        if(u <= f(x)/(C*g(x))):
            break
    U=generatingU()
    if(U <= 0.5):
            z= np.abs(x)
    else:
        z=- np.abs(x)
        
    fx.append(z) 
    #Normalization which apply to get the shiffted graph after mutate the sd & mean
    X=z+100             #the case of mean =100 &sd=1
    fx1.append(X)
    X2=100*z+100        #the case of mean =100 &sd=100
    fx2.append(X2)
    
#first case Normal (0, 1).
#plt.subplot(111)    
#plt.hist(fx,color='wheat',edgecolor = 'pink', bins = int(95/5),density='True')
#plt.show()

#second case  Normal (100, 1)
#plt.subplot(211)
fx2.sort()
plt.plot(fx2)
#x = np.linspace(50,150,100000)
#y = norm.pdf(x, loc=100, scale=1)
#plt.plot(range3,fx1)
#plt.plot(range1,fx1(range1))
#plt.hist(fx1,color='khaki',edgecolor = 'gray', bins = int(120/20),density='True')
#plt.show()
#Third case Normal with mean 100 and variance 100.
#plt.subplot(221)
#x = np.linspace(50,150,100000)
#y = norm.pdf(x, loc=100, scale=1)
#pylab.plot(x,y)
##plt.hist(fx2,color='olive',edgecolor = 'pink', bins = int(120/5),density='True',rwidth=10)
#plt.show()


    # for example

pylab.show()
   
