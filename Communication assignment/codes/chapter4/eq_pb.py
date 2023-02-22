from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


b=random.binomial(n=1, p=0.5, size=1000)
print(b)
sns.distplot(b, hist=False, label='binomial')

plt.savefig('../../figs/chapter4/eq_pb.pdf')
plt.savefig('../../figs/chapter4/eq_pb.png')
plt.show()

