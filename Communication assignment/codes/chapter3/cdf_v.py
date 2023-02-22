from matplotlib import pyplot as plt
from scipy.stats import uniform
import numpy as np


def samp(cdf):
    a, counts = np.unique(cdf, return_counts=True)
    add = np.cumsum(counts) #cumsum
    return a, add / add[-1]

randvar = np.loadtxt('../data_center/uni.dat', dtype='double')
#U and V given  

cdf_u = uniform.rvs(0,size=1000)
cdf_v=-2*np.log(1-cdf_u)

#x and y plots
horz, vert = samp(cdf_v)

horz = np.insert(horz, -1, horz[0])
vert = np.insert(vert, 0,-1 )

#line space
line=np.linspace(0,10,150)

plt.plot(line,1-np.exp(-line/2))
plt.grid(True)
plt.xlabel("$x$")
plt.ylabel("$F_X(x)$")
plt.legend(loc='best')
plt.title("CDF $(V)$") 
plt.savefig('../../figs/chapter3/cdf_v.png')
plt.savefig('../../figs/chapter3/cdf_v.pdf')
plt.show()


