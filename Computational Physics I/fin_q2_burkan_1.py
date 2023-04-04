import numpy as np
import matplotlib.pyplot as plt
from math import *
from fin_q2_burkan.py import monte_carlo_sampling

def like_hood_calculator(n,k):#k stands for the mean of the result_tot_np and n for the result_tot
    fin.result_tot = n
    l = 1
    for i in range(0,len(n)):
        l*= (np.exp(-k)*(k**result_tot[i]))/(factorial(int(result_tot[i])))
        r= np.log(l)
        return(r)
    lambd2= np.linspace(0.2,1,100)#Lambdas
    likely_hood=[]
    for i in lambda2:
        likely_hood.append(like_hood_calculator(result_tot_np,i))#lambda log likelihood values

    y=list(zip(lk,lambd2))
    q=sorted(y)#find lmax and sort

    Lmin= np.log(np.exp((q[-1][0])-0.5))
    Lmax= np.log(np.exp((q[-1][0])+0.5))
    print("Lmax value and our mean value: ",q[-1])
    print("Upper bound of the error interval: " , Lmax)
    print("Lower bound of the error interval: ", Lmin)

    plt.plot(lambd2,lk,'-r')
    plt.xlabel('lambda')
    plt.ylabel('Log-Likelihood')
    plt.title('Log-Likelihood Plot for Accident result_tot')
    plt.grid(True)


    plt.gcf().savefig("Likelihood graph.pdf")