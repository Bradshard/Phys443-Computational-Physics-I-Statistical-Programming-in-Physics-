from math import * 
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as pl



with open("Phys443-data.txt.txt") as inp:
    values = (list(zip(*(line.strip().split('\t') for line in inp)))) #By this we get an array with tuples in it which is our values but separated correctly.


a = len(values[0]) # easy to write letters are chosen for convenience.
b = len(values[1])
c = len(values[2])
d = len(values[3]) 

exam_grades_tot = 0 # all scores together
exam_grades_mean = 0 # will be counted after the for loop
exam_grades_std = 0 # will be measured in one of the for loops
summ_e = 0 # sum needed for standard deviation

laboratory_grades_tot = 0 # all scores together
laboratory_grades_mean = 0 # same as exam grades
laboratory_grades_std = 0 # same as exam grades
summ_l = 0 # sum needed for standard deviation

homework_grades_tot = 0 # all scores together
homework_grades_mean = 0 # same as exam grades
homework_grades_std = 0 # same as exam grades
summ_h = 0 # sum needed for standard deviation


attendance_grades_tot = 0 # all scores together
attendance_grades_mean = 0 # same as exam grades
attendance_grades_std = 0 # same as exam grades
summ_a = 0 # sum needed for standard deviation



for i in range(a):
	exam_grades_tot += int(values[0][i])

exam_grades_mean = exam_grades_tot/a

for w in range(b):
	laboratory_grades_tot += int(values[1][w])

laboratory_grades_mean = laboratory_grades_tot/b

for j in range(c):
	homework_grades_tot += int(values[2][j])

homework_grades_mean = homework_grades_tot/c

for k in range(d):
	attendance_grades_tot += int(values[3][k])

attendance_grades_mean = attendance_grades_tot/d

# all lengths may or may not be the same for all cases that's why I measured all in their own loops.

# standard deviation part.
for q in range(a):
	summ_e += (int(values[0][q]) - exam_grades_mean)**2

exam_grades_std = sqrt(summ_e/a)

for r in range(b):
	summ_l += (int(values[1][r]) - laboratory_grades_mean)**2

laboratory_grades_std = sqrt(summ_l/b)

for t in range(c):
	summ_h += (int(values[2][t]) - homework_grades_mean)**2

homework_grades_std = sqrt(summ_h/c)

for p in range(d):
	summ_a += (int(values[3][p]) - attendance_grades_mean)**2

attendance_grades_std = sqrt(summ_a/d)

print("for exam: {}, {}".format(exam_grades_mean , exam_grades_std))
print("for laboratory: {}, {}".format(laboratory_grades_mean, laboratory_grades_std))
print("for homework: {}, {} ".format(homework_grades_mean , homework_grades_std))
print("for attendance: {}, {}".format(attendance_grades_mean , attendance_grades_std))

