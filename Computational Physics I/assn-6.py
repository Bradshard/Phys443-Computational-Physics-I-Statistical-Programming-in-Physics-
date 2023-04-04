import csv
from math import *
import matplotlib.pyplot as plt
import numpy as np

phys =  open('accidents.csv', 'r')
reader = csv.reader(phys)

e = 2.71
a = []
summ = 0
nums = 0
val = 0
value_array = []
c = []

for i in range(447):
	value_array.append(0)
for i in range(132):
	value_array.append(1)
for i in range(42):
	value_array.append(2)
for i in range(21):
	value_array.append(3)
for i in range(3):
	value_array.append(4)
for i in range(2):
	value_array.append(5)
#Not too convenient but I got nervous and did this way.

for row in reader:
	a.append(row)

for i in range(0,len(a)):
	summ += int(a[i][1])*int(a[i][0])
	nums += int(a[i][1])

mean = summ/nums
L_poisson_dist = (e**(-mean))*1

for i in value_array:
	val += -log(factorial(i))

lnL = -nums*mean + log(mean)*summ - val

for i in range(1,nums):
	L_poisson_dist *= ((e**-mean)*(mean**value_array[i]))/(factorial(value_array[i]))
	c.append(log(L_poisson_dist))
print(L_poisson_dist)

	

p = np.linspace(0, 20, num = 646)
logL = c
dlogL = -2 * p + 20
fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(12, 8))
ax1.plot(p, logL, lw=2)
ax2.plot(p, dlogL, lw=2)
ax1.set_ylabel(r'$log \mathcal{L(\alpha)}$', rotation=0, labelpad=35, fontsize=15)
ax2.set_ylabel(r'$\frac{dlog \mathcal{L(\alpha)}}{d \alpha}$ ', rotation=0, labelpad=35,
fontsize=19)
ax2.set_xlabel(r'$\alpha$', fontsize=15)
ax1.grid(), ax2.grid()
plt.axhline(c='blue')
plt.axvline(x = mean, color='r', linestyle='--')
plt.axes(ax1)
plt.axvline(x = mean, color='r', linestyle='--')
plt.show()
