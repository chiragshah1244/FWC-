
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
#import subprocess
#import shlex
#end if

m=50 #m
maxl=10.0 #n
x = np.linspace(0,10,50)   
samp_len = int(1e6) 
prb = [] 
pdf = [] 
x1 = np.random.normal(0, 1, samp_len)
x2 = np.random.normal(0, 1, samp_len)
v = x1**2 + x2**2
print("x1^2+x2^2 =",v)
v_sq=np.sqrt(v)
print("root(x1^2+x2^2 =",v_sq)

for i in range(0,50):
	prb_ind = np.nonzero(v_sq < x[i]) 
	prb_n = np.size(prb_ind) 
	prb.append(prb_n/samp_len) 
	
pdf = np.gradient(prb, x, edge_order=2)

def sq_cdf(x):
  return 1-np.exp(-(x**2)/2)


def sq_pdf(x):
  return x*np.exp(-(x**2)/2)

	
plt.plot(x, pdf, 'o')             #  estimated PDF
plt.plot(x, sq_pdf(x))             #  theory PDF
plt.grid() 
plt.xlabel('$x_i$')
plt.ylabel('$p_X(x_i)$')
plt.legend(["Numerical value","Theoretical value"])

plt.savefig('../../figs/chapter5/sqroot_pdf.pdf')
plt.savefig('../../figs/chapter5/sqroot_pdf.png')

plt.show()

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/sqroot_pdf.pdf"))
#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter5/sqroot_pdf.pdf"))
#else
#plt.show() #opening the plot window
