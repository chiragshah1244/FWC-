import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
#import subprocess
#import shlex
#end if

#Let no of samples be 500

m=100 #range
n=10.0 #length
x = np.linspace(0,10.0,100)    
prb = []  #probability list
pdf = [] # pdf list
#defing X1 and X2
x1 = np.random.normal(0, 1, 500)
x2 = np.random.normal(0, 1, 500)
V = x1**2 + x2**2            #V = X1^2 + X2^2
trs= x.T

for i in range(0,m):
	prb_ind = np.nonzero(V < x[i]) #checking probability condition
	prb_n = np.size(prb_ind) #computing the probability
	prb.append(prb_n/500) #storing the probability values in a list
 
def sum_cdfa(x):
  return 1-np.exp(-(x)/2)
  
def sum_cdfb(x):
	return 1-np.exp(-(x))

def sum_cdfc(x):
	return 1-np.exp(-2*(x))

plt.plot(trs,prb,'o')   #numerical values
plt.plot(x, sum_cdfa(x),'m',marker='x')  #theory values
plt.plot(x, sum_cdfb(x),'r')
plt.plot(x, sum_cdfc(x))
plt.grid()          
plt.xlabel('<---$x$--->')
plt.ylabel('<---$F_V(x)$--->')

plt.legend(['simulated' , 'alpha=a(half)','alpha=b','alpha=c'])
plt.savefig('../../figs/chapter5/value_alfa.pdf')
plt.savefig('../../figs/chapter5/value_alfa.png')

plt.show()

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/value_alfa.pdf"))
#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/value_alfa.pdf"))
#else
#plt.show() #opening the plot window
