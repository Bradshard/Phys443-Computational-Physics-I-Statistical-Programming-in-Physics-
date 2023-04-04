import numpy as np
import matplotlib.pyplot as pl
data = np.array([[1.0 , 2.0 , 3.0 , 4.0],[2.2 , 2.9 , 4.3 , 5.2],[0.2 , 0.4 , 0.3 , 0.1]])
x1=sum(data[0])
y1=sum(data[1])
x1y1=sum(data[0]*data[1])

alpha = ((y1*sum(data[0]**2))-(x1y1*x1))/((len(data[0])*sum(data[0]**2))-((sum(data[0]))**2))

betha  = ((len(data[0])*x1y1)-(x1*y1))/(((len(data[0]))*(sum(data[0]**2)))-((sum(data[0]))**2))

D = ((sum((data[0]**2)/(data[2]**2)))*((sum(1/data[2]**2))))-((sum(data[0]/(data[2]**2)))**2)

sigmabetha = np.sqrt((sum(1/data[2]**2))*(1/D))

sigmaalpha = np.sqrt(sum((data[0]**2)/(data[2]**2))*(1/D))

chisquare = sum(((data[1]-((betha*data[0])+alpha))**2)/(data[2]**2))
print("chisquare = " , chisquare , "sigmaalpha = " , sigmaalpha , "sigmabetha = ", sigmabetha)
print("Since our chisquare bigger than 0.65 we can approximate as 0.65 and its probability is 72% and it is a good fit")
pl.scatter(data[0],data[1],c = "red")
pl.plot(data[0],((data[0]*betha)+alpha),"-b",label = " fit ")
pl.errorbar(data[0],data[1],yerr=data[2],ecolor="black",label= " data ")
pl.grid(True)
pl.xlabel("x values")
pl.ylabel("y values")
pl.title("least square fit and data graph")
pl.legend()
pl.gcf().savefig("Least Square Fit Graph.pdf")
print("alpha as constant value = ", alpha, "betha as the slope value =", betha)
