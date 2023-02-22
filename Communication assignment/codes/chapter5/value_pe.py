import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import scipy.stats as ss

#if using termux
import subprocess
import shlex
#end if

def root(x):
    return 0.5 - 0.5*(math.sqrt(x/(2+x)))

del_vals = np.linspace(0, 10, 11) #counts from 0 to 10 in division of 11 times

#simulation
#Let the simulation length be 100000
N = np.random.normal(0,1,100000)

val = []

for i in range(0, 11):

  delta = 10**(0.1*del_vals[i])
  
  d_arr=ss.rayleigh.rvs( math.sqrt((delta)/2),size=100000)
  val_mug = 0
  for j in range(100000):
    if d_arr[j]+N[j]<0:
      val_mug=val_mug+1 
  val_mug /= 100000
  val.append(val_mug)

plt.semilogy(del_vals.T, val, 'o')
plt.xlabel('$delta$ in dB')
plt.ylabel('$P_e(delta)$')
plt.grid()

plt.savefig('../../figs/chapter5/value_pe.pdf')
plt.savefig('../../figs/chapter5/value_pe.png')
plt.show()
