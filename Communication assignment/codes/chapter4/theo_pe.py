import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt



def pe_fun(x):
    return 0.5*mp.erfc(x/mp.sqrt(2))
    
#Defining the size and its weight 
n_dB = np.linspace(-10, 20, 50)
n = 50

slot = []
 
N = np.random.normal(0, 1, 100000)

fix = []
for i in range(0, n):
    con = 10**(0.1*n_dB[i])
    val = mp.sqrt(con) 
    num=val+N                                 #adding numerical values

    err_n = np.size(np.nonzero(num < 0))
    slot.append(err_n/100000)
   
    fix.append(pe_fun(mp.sqrt(con)))
    
    trans=n_dB.T 

plt.semilogy(trans, fix, label = 'Theoritical')
plt.semilogy(trans, slot, 'o',  label = 'Numerical')
plt.xlabel("<---$dB$--->")
plt.ylabel("<---$P_e(dB)$--->")
plt.legend()
plt.grid()

plt.savefig('../../figs/chapter4/theo_pe.pdf')
plt.savefig('../../figs/chapter4/theo_pe.png')

#if using termux
#subprocess.run(shlex.split("termux-open ../../figs/chapter4/theo_pe.pdf"))
#else
plt.show() #opening the plot window
