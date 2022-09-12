#program to construct a right triangle using its base and sum of other two sides
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts

sys.path.insert(0,'/sdcard/IIT_H/CoordGeo')
#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

#Input parameters

s=18  #sum=hypo+side=18
b=12  #base=12

i=((s**2)-(b**2))/(2*s)
k= int(i)

O = np.array(([0,0]))
B = np.array(([12,0]))
A = np.array(([0,k]))

print("The coordinates of A is A",A)
print("From given base and sum")
print("The coordinates of O is O",O) 
print("The coordinates of B is B",B)

#Generating all lines
x_OA = line_gen(O,A)
x_AB= line_gen(A,B)
x_BO = line_gen(B,O)
#
#
#Plotting all lines
plt.plot(x_OA[0,:],x_OA[1,:],label='$a$')
plt.plot(x_AB[0,:],x_AB[1,:],label='$c$')
plt.plot(x_BO[0,:],x_BO[1,:],label='$b$')
#
#
#Labeling the coordinates
tri_coords = np.vstack((O,A,B)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O','A','B']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/sdcard/IIT_H/sol/matrix2112..pdf')
subprocess.run(shlex.split("termux-open '/sdcard//IIT_H/sol/matrix2112..pdf'")) 
#else
#plt.show()
