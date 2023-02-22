#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

maxrange=50
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)    #points on the x axis
simlen = int(1e6) #number of samples
err = [] 
h = 2*maxlim/(maxrange-1);
randvar = np.loadtxt('../data_center/gau.dat', dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
#ploting the CDF
plt.plot(x.T,err)
plt.grid()      
plt.xlabel('<----$x$---->')
plt.ylabel('<----$F_X(x)$---->')

plt.savefig('../../figs/chapter3/gau_cdf.pdf')
plt.savefig('../../figs/chapter3/gau_cdf.png')

plt.show()
