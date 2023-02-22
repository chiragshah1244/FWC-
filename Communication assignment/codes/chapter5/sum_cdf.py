# Let X1 ∼N(0,1)and X2 ∼N(0,1).Plot the CDF and PDF of V = X1^2 + X2^2
#cdf
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
 
def sum_cdf(x):
  return 1-np.exp(-(x)/2)

plt.plot(trs,prb,'o')   #numerical values
plt.plot(x, sum_cdf(x))  #theory values
plt.grid()          
plt.xlabel('<---$x$--->')
plt.ylabel('<---$F_V(x)$--->')

plt.savefig('../../figs/chapter5/sum_cdf.pdf')
plt.savefig('../../figs/chapter5/sum_cdf.png')

plt.show()

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/sum_cdf.pdf"))
#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/sum_cdf.pdf"))
#else
#plt.show() #opening the plot window
