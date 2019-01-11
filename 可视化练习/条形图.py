import matplotlib.pylab as plt
import numpy as np

n = 12
x1 = np.arange(n)
Y1 = (1-x1/float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1-x1/float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(x1, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(x1, -Y2, facecolor='#9999ff', edgecolor='white')

#zip 可以返回两个数值-->即把x,y组合成(x,y)
#plt.text (x+0.4,y+0.05)即输出的位置坐标，‘%.2f'%y为数值，ha：水平对齐方式
#va：垂直对齐方式
for x,y in zip(x1, Y1):
    plt.text(x+0.04, y+0.05,'%.2f'%y,ha='center',va='bottom')
for x,y in zip(x1, Y2):
    plt.text(x+0.04, -y-0.05,'%.2f'%y,ha='center',va='top')

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()