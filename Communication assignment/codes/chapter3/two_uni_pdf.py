#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp

#Importing numpy, scipy, mpmath and pyplot
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
pdf_x = np.linspace(-4.0,4.0,max_v)
#pdf_x = np.linspace(-1.0,4.0,max_v)

for i in range(0,max_v):

    #in checking probability condition
	lis_cond = np.nonzero(load < pdf_x[i])

    #compution of probability
	lis_comp = np.size(lis_cond) 

    #storing proby value in list
	lis.append(lis_comp/n_samp)
	
pdf = np.gradient(lis, pdf_x, edge_order=2)
	
tri_dist = np.piecewise(pdf_x, [pdf_x < 0, ((pdf_x >= 0) & (pdf_x < 1)), ((pdf_x >= 1) & (pdf_x < 2)), pdf_x >= 2], [0, lambda pdf_x: pdf_x, lambda pdf_x: 2-pdf_x, 0])

#plt.plot(pdf_x,pdf,'o')
plt.plot(pdf_x,tri_dist)  
#plt.plot(pdf_x,pdf,'o')  

plt.xlabel('<----$x_i$---->')
plt.ylabel('<----$p_X(x_i)$---->')
#plt.legend(["Numerical plot","Theory valu"])
plt.grid()  

plt.savefig('../../figs/chapter3/tri_dist_pdf.pdf')
plt.savefig('../../figs/chapter3/tri_dist_pdf.png')

plt.show()

