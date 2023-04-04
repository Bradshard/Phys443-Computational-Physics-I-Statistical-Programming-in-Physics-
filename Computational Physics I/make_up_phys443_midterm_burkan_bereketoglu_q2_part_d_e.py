import numpy as np
import matplotlib.pyplot as pl

f = open ('Phys443-data.txt.txt' , 'r')
l=[]
l = np.array([(line.split()) for line in f])#I read the data.
k=len(l)
print(k)
s=len(l[1])
sol=[]
for i in range(1,k):
    sol.append([])
    for p in range(0,2):
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
dfe=215
dft = dfr+dfe
ssr = ((sxy1(sol2,0,1))**2)/sxx1(sol2,0)
sst = sxx1(sol2,1)
sse = sst-ssr
msr = ssr
mse = sse/215
f = msr/mse
r_square = ssr/sst
print(["Source" , "df" , "SS" , "MS" , "F"])
print(["Regression" , 1 , ssr, msr, f])
print(["ERROR" , 217-2 , sse , mse])
print(["Total" , 216 , sst])
#i choose first midterm results x variable   
pl.scatter(sol2[:,0],sol2[:,1], label='data points')
pl.plot(a + b*sol2[:,0],sol2[:,0],'-r',label='fit curve')
pl.grid(True)
pl.legend()
pl.xlabel('first midterm')
pl.ylabel('second midterm')
print("r^2 = ", r_square)
pl.gcf().savefig("regression graph.pdf")