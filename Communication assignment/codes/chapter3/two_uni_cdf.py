import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

#max value to plot
max_v=150

#no of samples
n_samp = int(1e6) 

#list
lis = []

load = np.loadtxt('../data_center/u_1.dat',dtype='double') + np.loadtxt('../data_center/u_2.dat',dtype='double')

#x axis plots
cdf_x = np.linspace(-4.0,4.0,max_v)
#cdf_x = np.linspace(-1.0,4.0,max_v)

for i in range(0,max_v):

    #in checking probability condition
	lis_cond = np.nonzero(load < cdf_x[i])

    #compution of probability
	lis_comp = np.size(lis_cond) 

    #storing proby value in list
	lis.append(lis_comp/n_samp)
	
pdf = np.gradient(lis, cdf_x, edge_order=2)

tri_dist = np.piecewise(cdf_x, [cdf_x < 0, ((cdf_x >= 0) & (cdf_x < 1)), ((cdf_x >= 1) & (cdf_x < 2)), cdf_x >= 2], [0, lambda cdf_x: cdf_x**2/2, lambda cdf_x: 2*cdf_x - cdf_x**2/2 - 1, 1])

plt.plot(cdf_x,lis,'o') 
plt.plot(cdf_x,tri_dist) 	
plt.grid()          
plt.xlabel('<----$x$---->')
plt.ylabel('<----$F_X(x)$---->')
plt.legend(["Num plot","Theory values"])

plt.savefig('../../figs/chapter3/tri_dist_cdf.pdf')
plt.savefig('../../figs/chapter3/tri_dist_cdf.png')

plt.show()


#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter3/tri_dist_cdf.pdf"))
#else
#plt.show() #opening the plot window
