import numpy as np
import matplotlib.pyplot as pl
f = open ('Phys443-data.txt.txt' , 'r')

data=[]
data = np.array([(line.split()) for line in f])#I read the data.

data_std = np.linspace(18,21,217)
D = 0
data_x = []
data_y = []
for i in range(len(data)):
	data_x.append(int(data[i][0]))

for i in range(len(data)):
	data_y.append(int(data[i][1]))

x1=sum(data_x)
x1_sq = 0
y1=sum(data_y)
x1y1 = 0
for i in range(len(data)):
	x1y1 += data_x[i]*data_y[i]
for i in range(len(data)):
	x1_sq += data_x[i]**2

alpha = ((y1*x1_sq)-(x1y1*x1))/((len(data)*x1_sq)-((x1)**2))

betha  = ((len(data)*x1y1)-(x1*y1))/(((len(data)*(x1_sq))-((x1)**2)) 

for i in range(len(data)):
	D = (((sum((data_x[i]**2)/(data_std[i]**2)))*((sum(1/data_std[i]**2))))-((sum(data_x[i]/(data_std[i]**2)))**2))

sigmabetha = np.sqrt((sum(1/data_std**2))*(1/D))

sigmaalpha = np.sqrt(sum((data_x**2)/(data_std**2))*(1/D))

chisquare = sum(((data_y-((betha*data_x)+alpha))**2)/(data_std**2))
print("chisquare = " , chisquare , "sigmaalpha = " , sigmaalpha , "sigmabetha = ", sigmabetha)
print("Since our chisquare bigger than 0.65 we can approximate as 0.65 and its probability is 72% and it is a good fit")
pl.scatter(data_x,data_y,c = "red")
pl.plot(data_x,((data_x*betha)+alpha),"-b",label = " fit ")
pl.errorbar(data_x,data_y,ecolor="black",label= " data ")
pl.grid(True)
pl.xlabel("x values")
pl.ylabel("y values")
pl.title("least square fit and data graph")
pl.legend()
pl.gcf().savefig("Least Square Fit Graph.pdf")
print("alpha as constant value = ", alpha, "betha as the slope value =", betha)"""