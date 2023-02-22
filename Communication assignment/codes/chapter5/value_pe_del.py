import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import scipy.stats as ss

#if using termux
#import subprocess
#import shlex
#end if

def root(x):
    return 0.5 - 0.5*(math.sqrt(x/(2+x)))

del_vals = np.linspace(0, 10, 11)

val = []

#simulation length be 100000.
N = np.random.normal(0,1,100000)

er = [] #probability

for i in range(0, 11):

  gamma = 10**(0.1*del_vals[i])
  
  d_arr=ss.rayleigh.rvs( loc = 0, scale = math.sqrt((gamma)/2),size=100000)
  val_mug = 0
  for j in range(100000):
    if d_arr[j]+N[j]<0:
      val_mug=val_mug+1
        
  val_mug /= 100000
  er.append(val_mug)
  val.append(root(gamma))

plt.semilogy(del_vals.T, er, 'o')
plt.semilogy(del_vals.T, val, '-')
plt.xlabel('$delta$ in dB')
plt.ylabel('$P_e(delta)$')
plt.legend(["Theoretical value", "Simulated value"])
plt.grid()

plt.savefig('../../figs/chapter5/value_pe_del.pdf')
plt.savefig('../../figs/chapter5/value_pe_del.png')
plt.show()
