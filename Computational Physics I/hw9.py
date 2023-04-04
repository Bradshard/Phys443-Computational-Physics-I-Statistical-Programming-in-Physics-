import numpy as np
import matplotlib.pyplot as plt
import csv

phys =  open('data15.csv', 'r')
reader = csv.reader(phys)
print(reader)
items = []
mt1 = []
mt2 = []
for row in reader:
    items.append(row)
for i in range(1,len(items)):
    mt1.append(items[i][0])
for i1 in range(1,len(items)):
    mt2.append(items[i1][1])
print(mt2[1])
"""
k=len(l)
s=len(l[1])
sol=[]
for i in range(1,k):
    sol.append([])
    for p in range(0,s):
      sol[i-1].append(int(l[i][p]))
      #the read that should be in a matrix i make the stuff using numpy.array
sol2=np.array(sol)

def calc_mean(n):#his is mean calculator
    ow=len(n)
    sql=0
    for i in range(0,ow):
        sql+=(n[i])/ow
    return sql

def sxx1(n,p):#This is for S subxx
    lp=len(n[:,p])
    res=0
    res+=sum((n[:,p])**2) - (((sum(n[:,p]))**2)/lp)
    return(res)
def sxy1(n,l,k):#This is for S subxy
    lp=len(n[:,l])
    a1=0
    for i in range(0,lp):
        a1+= n[:,l][i]*n[:,k][i]
    b1=(sum(n[:,l])*sum(n[:,k]))/lp
    res= a1-b1
    return res
b = sxy1(sol2,0,1)/sxx1(sol2,0)
a = calc_mean(sol2[:,1])-(b*calc_mean(sol2[:,0]))

dfr=1
dfe=98
dft = dfr+dfe
ssr = ((sxy1(sol2,0,1))**2)/sxx1(sol2,0)
sst = sxx1(sol2,1)
sse = sst-ssr
msr = ssr
mse = sse/98
f = msr/mse
r_square = ssr/sst
print(["Source" , "df" , "SS" , "MS" , "F"])
print(["Regression" , 1 , ssr, msr, f])
print(["ERROR" , 100-2 , sse , mse])
print(["Total" , 100-1 , sst])
#i choose first midterm results x variable   
plt.scatter(sol2[:,0],sol2[:,1], label='data points')
plt.plot(a + b*sol2[:,0],sol2[:,0],'-r',label='fit curve')
plt.grid(True)
plt.legend()
plt.xlabel('first midterm')
plt.ylabel('second midterm')
print("r^2 = ", r_square)
plt.gcf().savefig("regression graph.pdf")"""