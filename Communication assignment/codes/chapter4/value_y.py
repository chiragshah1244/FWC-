import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


n = 100
X = np.random.binomial(1, 0.5,n)*2-1


N = np.random.normal(0, 1,n)

a = 5
A = (0.1*5)**10
Y = A*X + N


sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')


print(Y)
plt.show()


