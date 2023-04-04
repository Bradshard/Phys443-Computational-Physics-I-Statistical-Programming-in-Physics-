import numpy as np
import matplotlib.pyplot as pl
import math as mt
data=[]
for i in range(0,447):
    data.append(0)
for o in range(0,132):
    data.append(1)
for l in range(0,42):
    data.append(2)
for p in range(0,21):
    data.append(3)
for y in range(0,3):
    data.append(4)
for r in range(0,2):
    data.append(5)
data1 = np.array(data)

nu=np.mean(data1)
def like_hood_calculator(n,k):#k stands for the mean of the data1 and n for the data
    l = 1
    for i in range(0,len(n)):
        l*= (np.exp(-k)*(k**data[i]))/(mt.factorial(data[i]))
    r= np.log(l)
    return(r)
lambd2= np.linspace(0.2,1,100)#This is our lambda values
likely_hood=[]
for i in lambd2:
    likely_hood.append(like_hood_calculator(data1,i))#we found our lamda values log likelihood function values
lk=np.array(likely_hood)#likelihood function values array

y=list(zip(lk,lambd2))
q=sorted(y)#to find the Lmax i made a list then sort it.

Lmin= np.log(np.exp((q[-1][0])-0.5))
Lmax= np.log(np.exp((q[-1][0])+0.5))
print("Lmax value and our mean value: ",q[-1])
print("Upper bound of the error interval: " , Lmax)
print("Lower bound of the error interval: ", Lmin)

pl.plot(lambd2,lk,'-r')
pl.xlabel('lambda')
pl.ylabel('Log-Likelihood')
pl.title('Log-Likelihood Plot for Accident Data')
pl.grid(True)


pl.gcf().savefig("Likelihood graph.pdf")
