import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(-3, 3, 50)
b = a ** 2
c = 2 * a

plt.figure()
#可以给曲线设置代表的参数
l1, = plt.plot(a, b, label='up')  #label设置曲线的名称
l2, = plt.plot(a, c, color='red', linewidth=1.0, linestyle='--', label='down')

plt.xlim((-1, 2))  #x坐标轴的范围规定
plt.ylim((-2, 3))  #y坐标轴的范围规定

plt.xlabel('this is x')  #设置x轴的名称
plt.ylabel('this is y')  #设置y轴的名称

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)  #设置x轴的刻度大小
plt.yticks([-2, -1.5, 0, 2, 3],
           ['really/ bad', 'bad', 'normal', 'good', 'very good'])    #设置各刻度所对应的名称

#输出图例
#或者直接用plt.legend()
plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best')   #设置图例
plt.show()