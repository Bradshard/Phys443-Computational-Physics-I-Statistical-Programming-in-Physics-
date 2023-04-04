from random import randint
import numpy as np


M_0 = 784 #MeV
Gamma = 12 #MeV

#Creating zero arrays for reachability.
weighted_Data = np.zeros(1000)
data = np.zeros(1000)

#Creating random events over the range given.
for i in range(0,1000):
    random_Event = randint(748,820) #Unit is MeV
    data[i] = randomEvent
    weighted_Data[i] = (Gamma/2)/((data[i] - M_0)**2 + (Gamma/2)**2) #Weighting the data with the given B function.
    