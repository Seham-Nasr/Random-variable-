# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 07:14:14 2019

@author: SehamM
"""

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

import numpy as np
import math
import random 
import matplotlib.pyplot as plt

print ('\n ______________Generated Random variable ___________\n   ')
n=input('please enter N:')
n=int(n)
s = np.random.uniform(0,1,n)
#np.all(s >= 0)
#np.all(s < 1)
#plt.title("Standard Uniform distribution (pdf)")
#count, bins, ignored = plt.hist(s, 1, density=True)
#plt.plot(bins, np.ones_like(bins), linewidth=5, color='r')
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.show()


#value=numpy.random.uniform(0,1,n)
#print ('\n     u(0,1) :   ',value)
##plt.title("Standard Uniform distribution")
##plt.hist(value)
##plt.xlabel("Value")
##plt.ylabel("frequency")
##plt.show()
#rv=np.random.uniform(-5,100,n)
#[min,max]=[-5,100]
#print ("This is uniform function way 1: (x-a)/(b-a)")
#un=(rv-min)/(max-min)
#print("uniform dist.  ",un)
#np.all(rv >= -5)
#np.all(rv < 100)
#plt.title("  Uniform distribution (pdf)")
#count, bins, _ = plt.hist(rv, 1, density=True)
#plt.plot(bins, np.ones_like(bins)/(max-min), linewidth=2, color='r')
#plt.xlabel("x")
#plt.ylabel("f(x)")
#plt.show()
#cdf=np.cumsum(count)
#cdf /= cdf[-1]
#plt.plot(bins[1:],cdf)
#plt.plot(bins[1:], (bins[1:]-min)/(max-min),linewidth=5, color='r')
#plt.show()
#plt.title("Uniform distribution")
#plt.plot(un)
#plt.xlabel("value")
#plt.ylabel("frequency")
#plt.show()
#mn=1 /(max-min)
#print(",,,,,,,,,,,,,,,\n",mn)
#plt.title("Uniform distribution")
#plt.hist(mn)
#plt.xlabel("value")
#plt.ylabel("frequency")
#plt.show()
#print ("\nThis is uniform, mapping way 2:")
#rm = s*(max-min) + min
#print('uniform(',min,',',max,'): ',rm,sep='')
#count, bins, ignored = plt.hist(rm, 15, density=True)
#plt.plot(bins, np.ones_like(bins)/(max-min), linewidth=2, color='r')
#plt.show()
##b-Exponential with mean = 100
#print('\nExponential with mean =100 is :  ')
#for u in value:
#    x = -(math.log(1-u))/100
#    print(x)
#
#
#   
import numpy
import matplotlib.pyplot as plt


Min = -5
Max = 100
r = numpy.random.uniform(Min, Max, n)

num_bins = Max - Min
counts, bins, _ = plt.hist(r, num_bins, density=True)

plt.ylabel('PDF')
plt.plot(bins, numpy.ones_like(bins)/(Max-Min), linewidth=2, color='r')
plt.show()

cdf = numpy.cumsum(counts)
cdf /= cdf[-1]
    
plt.plot(bins[1:], cdf)
plt.plot(bins[1:], (bins[1:]-Min)/(Max-Min), linewidth=1, color='r')
plt.title("  Uniform distribution (CDF)")
plt.ylabel('F(x)')
plt.xlabel('x')
plt.show()
