#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

x = np.linspace(-3,3,30)    #points on the x axis
simlen = int(1e6)           #number of samples
err = []                    

randvar = np.loadtxt('../data_center/uni.dat', dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) 
	err_n = np.size(err_ind) 
	err.append(err_n/simlen) 


y=np.piecewise(x,[x<0,(x>=0)&(x<=1),x>1],[0,lambda x:x,1])
plt.scatter(x.T,err)
plt.plot(x,y,'gray') 
plt.xlabel('<---------$x$-------->')
plt.ylabel('<----------$F_X(x)$--------->')
plt.legend(["Numerical value","Theoritical value"])
plt.grid()

plt.savefig('../../figs/chapter3/cdf_plot.pdf')
plt.savefig('../../figs/chapter3/cdf_plot.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter3/cdf_plot.pdf"))
#else
plt.show() #opening the plot window
