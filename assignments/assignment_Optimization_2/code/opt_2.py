#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Algo from Wikipedia
#Solving a mensuration optimization problem using 
#Gradient Descent

#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *


import sys                                          #for path to external scripts
sys.path.insert(0,'/home/chirag/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

def S(l):
	return  280+180*(l+4/l)


#Gradient Descent
cur_x = 2 # The algorithm starts at x=2
gamma = 0.001 # step size multiplier
precision = 0.00000001
previous_step_size = 1 
max_iters = 100000000 # maximum number of iterations
iters = 0 #iteration counter

df = lambda l: 180*(1-4/l**2)


while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x -= gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1
min_val=S(cur_x,)
print("Minimum value of f(x) is ", min_val, "at","l =",cur_x)

label_str = "$4x^3 - 22x^2 + 24x$"
#Plotting f(x)
x=np.linspace(0.1,10,100)
y=S(x)
plt.plot(x,y)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
#plt.legend()
plt.savefig('/home/chirag/Pictures/img/optimization_advance2.pdf')

