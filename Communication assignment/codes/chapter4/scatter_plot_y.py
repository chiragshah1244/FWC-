import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt

#if using termux
#import subprocess
#import shlex
#end if

a = 5
A=10**(0.1*a);

size = int(3000)
n= np.random.normal(0, 1, size)

v = [-1, 1] 
pb = [0.5, 0.5]

X=np.random.choice(v, size, p=pb)

x_up = np.extract(X==1, X)
x_down = np.extract(X==-1, X)
n_up = np.extract(X==1, n)
n_down = np.extract	(X==-1, n)
y_up = A*x_up + n_up
y_down = A*x_down + n_down

plt.scatter(np.arange(y_up.shape[0]),y_up)
plt.scatter(np.arange(y_down.shape[0]),y_down)

plt.plot(np.linspace(-10, 50, 10),np.zeros(10), color='black')
plt.grid()

plt.legend(["$y.up$","$y.down$"])
plt.savefig('../../figs/chapter4/scatter_plot_y.pdf')
plt.savefig('../../figs/chapter4/scatter_plot_y.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter4/scatter_plot_y.pdf"))
#else
plt.show() 
