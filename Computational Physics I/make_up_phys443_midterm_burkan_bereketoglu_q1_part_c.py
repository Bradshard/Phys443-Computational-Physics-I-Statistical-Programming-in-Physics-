from random import uniform
import numpy as np
import math
import matplotlib.pyplot as plt

#Probability Density Function for the given function and for calculating the log-likelihood
def PDF(mass,gamma,mass_Zero):
    summation = 0
    for i in range(0,len(mass)):
        summation += math.log((gamma/2)/((mass[i]-mass_Zero)**2 + (gamma/2)**2))
    return summation


M0 = 784 #MeV
Gamma = 12 #MeV
data_Count = 1000

data = np.zeros(data_Count)
masses = np.zeros(data_Count)


for i in range(0,data_Count):
    random_Event = uniform(-90,90) #Unit is MeV
    data[i] = random_Event
    masses[i] = math.tan(math.radians(data[i]))*(Gamma/2) + M0

#Creating empty arrays for storing numbers
mass_Zero_Guesses = np.arange(780,790,0.01)
gamma_Guesses = np.arange(8,16,0.01)
varying_Masses = []
varying_Gamma = []

#Store LnLikelihood for quantities with varying arguments.
for i in mass_Zero_Guesses:
    varying_Masses.append(PDF(masses,Gamma,i))

varying_Masses = np.array(varying_Masses) #turning lists into numpy arrays.

for j in gamma_Guesses:
    varying_Gamma.append(PDF(masses,j,M0))

#Ordering the values by making (x,y) sets and then sorting from small to big for future conve
sorting_List1 = list(zip(varying_Masses, mass_Zero_Guesses))
sorting_List2 = list(zip(varying_Gamma, gamma_Guesses))

sorting_List1 = sorted(sorting_List1)
sorting_List2 = sorted(sorting_List2)

maximum_Mass = sorting_List1[-1][1]
maximum_Gamma = sorting_List2[-1][1]

print("Mass Estimated with MLM: {:.2f}".format(maximum_Mass))
print("Gamma Estimated with MLM: {:.2f}".format(maximum_Gamma))

#Plotting
plt.figure(1)
plt.plot(mass_Zero_Guesses,varying_Masses,label = "MLM_Method")
plt.scatter(maximum_Mass,sorting_List1[-1][0],label="Maximum_Point",color = "red")
plt.title("MLM method for Finding Mass")
plt.xlabel("Masses")
plt.ylabel("Log Likelihood")
plt.grid()
plt.legend()
plt.savefig("Mass & LnLikelihood")

plt.figure(2)
plt.plot(gamma_Guesses,varying_Gamma,label = "MLM_Method")
plt.scatter(maximum_Gamma,sorting_List2[-1][0],label="Maximum_Point",color = "red")
plt.title("MLM method for Finding Gamma")
plt.xlabel("Gamma Values")
plt.ylabel("Log Likelihood")
plt.grid()
plt.legend()
plt.savefig("Gamma & LnLikelihood")