# -*- coding: utf-8 -*-


#Importing modules
import numpy as np
import matplotlib.pyplot as plt
from random import uniform as uni
import math




#numpy.random.uniform doesn't include endpoints 
#therefore I used random.uniform which includes even though I guess 
#endpoints can be neglectible in a good random distribution


steps = 10000 #number of random numbers generated
binCount = 30# Count of Histogram bins


#Setting 2 numpy array with full of zeros
randSet1, randSet2 = np.zeros([2,steps],dtype = float), np.zeros([2,steps],dtype = float)


for i in range(steps):
    #This creates 2 random numbers for 2 PDF then stores it into their
    #respective arrays.
    x1 = uni(0,1) 
    x2 = uni(0,1)
    randSet1[0][i] =  x1
    randSet2[0][i] = x2
    
    #Producing PDF with method of transformation
    randSet1[1][i] = np.log(1-(1-np.e**(-2))*x1)/(-2)
    randSet2[1][i] = x2**(1 / 3) 


 


#Creating 2 subplots, one for random numbers and one for PDF's
fig = plt.figure(figsize=(13,5))
figX = fig.add_subplot(1,2,1)
figY = fig.add_subplot(1,2,2)


#Histogram for random numbers
figX.hist([randSet1[0],randSet2[0]],binCount, label = \
['PDF 1 (Exponential)','PDF 2 (Polynomial)'], color = ['green','purple'])
figX.set_xlabel('Random Entries [0,1]')
figX.legend(loc = 'upper right')


#Histogram for PDF's
figY.hist([randSet1[1],randSet2[1]],binCount \
,label = ['PDF 1 (Exponential)', 'PDF 2 (Polynomial)'], color = ['green','purple'])
figY.set_xlabel('PDF')
figY.legend(loc = 'upper right')






plt.show()