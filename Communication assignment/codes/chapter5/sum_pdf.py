# Let X1 ∼N(0,1)and X2 ∼N(0,1).Plot the CDF and PDF of V = X1^2 + X2^2
#pdf
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
x = np.linspace(0,n,m)    
prb = []  #probability list
pdf = [] # pdf list
sam=50000
#defing X1 and X2
x1 = np.random.normal(0, 1, sam)
x2 = np.random.normal(0, 1, sam)
V = x1**2 + x2**2            #V = X1^2 + X2^2

for i in range(0,m):
	prb_ind = np.nonzero(V < x[i]) #checking probability condition
	prb_n = np.size(prb_ind) #computing the probability
	prb.append(prb_n/sam) #storing the probability values in a list
	
pdf = np.gradient(prb, x, edge_order=2)

def sum_pdf(x):
  return np.exp(-x/2)/2

vec_chi=scipy.vectorize(sum_pdf)

plt.plot(x.T,pdf,'o')             # plotting estimated PDF
plt.plot(x, vec_chi(x))          #Theory values 
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical value","Theoretical value"])

plt.savefig('../../figs/chapter5/sum_pdf.pdf')
plt.savefig('../../figs/chapter5/sum_pdf.png')

plt.show()

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/sum_pdf.pdf"))
#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/sum_pdf.pdf"))
#else
#plt.show() #opening the plot window

