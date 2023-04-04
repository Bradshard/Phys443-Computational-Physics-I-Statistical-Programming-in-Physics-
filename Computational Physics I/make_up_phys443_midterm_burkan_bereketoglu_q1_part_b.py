from random import uniform
import numpy as np


M0 = 784 #MeV
Gamma = 12 #MeV
B0 = 1/(Gamma/2)
data_Count = 1000 # for future convenience

data = np.zeros(data_Count)
on_hold = [] #List of numbers that are not eliminated

for i in range(0,data_Count):
    randoms = uniform(748,820) #Unit is MeV
    data[i] = randoms

#Through here similar to the part a.

for i in range(0,data_Count):
    Hold_it = True
    B = (Gamma/2)/((data[i] - M0)**2 + (Gamma/2)**2)
    
    if B/B0 <= uniform(0,1):
        Hold_it = False #This value may be used if and only if there is not any other random number that is bigger than this.
        
    if Hold_it == True:
        on_hold.append(data[i]) 
    
   
for i in range(0,len(on_hold)):
    print("{:.2f}".format(on_hold[i]))
    
