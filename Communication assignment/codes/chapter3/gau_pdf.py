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
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
randvar = np.loadtxt('../data_center/gau.dat', dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) 
	err_n = np.size(err_ind) 
	err.append(err_n/simlen) 
	
pdf = np.gradient(err, x, edge_order=2)

#for i in range(0,maxrange-1):
#	test = (err[i+1]-err[i])/(x[i+1]-x[i])
#	pdf.append(test) #storing the pdf values in a list

def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.4)

vec_gauss_pdf = scipy.vectorize(gauss_pdf)
#x=x[0:(maxrange-1)].T
#Plotting PDF
plt.plot(x,pdf,'o')             
plt.plot(x,vec_gauss_pdf(x))    # plotting theoretical PDF
plt.grid() #creating the grid
plt.xlabel('<----$x_i$---->')
plt.ylabel('<----$p_X(x_i)$---->')
plt.legend(["Numerical","Theory"])

plt.savefig('../../figs/chapter3/gau_pdf.pdf')
plt.savefig('../../figs/chapter3/gau_pdf.png')

plt.show()

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter3/gau_cdf.pdf"))
#subprocess.run(shlex.split("termux-open ../../figs/chapter3/gau_pdf.pdf"))
#else
#plt.show() #opening the plot window
