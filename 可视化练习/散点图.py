import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

#color map,通过映射，不同的数值对应不同的颜色，
#此时s为size，c为color，值为一个序列，对应一个cmap
#alpha为透明度
plt.scatter(X, Y, s=75, c=T, alpha=0.5)

plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
plt.xticks(())
plt.yticks(())

plt.show()