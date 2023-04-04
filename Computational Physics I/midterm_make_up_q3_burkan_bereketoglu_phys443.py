from math import *
import numpy as np
import matplotlib.pyplot as pl
from sympy.solvers import solve

i = [7,3,4,6,1] # for the counter 

def likelihood_function(data,tau): # likelihood_function
	tap = 1
	for j in range(len(data)):
		tap *= (1/tau)*e**(-data[j]/tau)
	return tap

#likelihood function is the function above due to this is being an exponential decay.

def ln_likelihood_function(data,tau):
	tap = 1
	for j in range(len(data)):
		tap *= (1/tau)*e**(-data[j]/tau)
	ln_tap = np.log(tap)
	return ln_tap

lambda_2 = np.linspace(0.1,7,500) # in a wide range we can have better understanding on what is the maximum value.

lnL = []
for p in lambda_2:
	lnL.append(ln_likelihood_function(i,p))
lk = np.array(lnL)

y = list(zip(lk,lambda_2))
q = sorted(y)
Lmin =  np.log(np.exp((q[-1][0])-0.5))
Lmax = np.log(np.exp((q[-1][0])+0.5))

print("Lmax value and our mean value: ", q[-1])

pl.plot(lambda_2,lk,'-r')
pl.xlabel('lambda')
pl.ylabel('Log-Likelihood')
pl.title('Log-Likelihood Plot for Unstable Particle Make-Up')
pl.grid(True)


pl.gcf().savefig("Likelihood graph.pdf")