import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(-3, 3, 50)
b = a ** 2
c = 2 * a

plt.figure(1)
plt.plot(a, c, color='red', linewidth=1.0, linestyle='--')  #设置输出的图像的颜色、粗细、样式

plt.figure(2, (8, 5))  #设置输出的画布的大小
plt.plot(a, b)
plt.plot(a, c, color='red', linewidth=1.0, linestyle='--')

plt.xlim((-1, 2))  #x坐标轴的范围规定
plt.ylim((-2, 3))  #y坐标轴的范围规定

plt.xlabel('this is x')  #设置x轴的名称
plt.ylabel('this is y')  #设置y轴的名称

new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)  #设置x轴的刻度大小
plt.yticks([-2, -1.5, 0, 2, 3],
           ['really/ bad', 'bad', 'normal', 'good', 'very good'])    #设置各刻度所对应的名称

#坐标轴的移动
#获取坐标轴,默认有4个轴，可以通过ax=plt.gca()获取4个轴：top、bottom、left、right
ax = plt.gca()
#设置右边框和头部边框的颜色设置为空
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#移动下面和左边的轴到指定位置
#ax.spines['bottom']获取底部的轴，通过set_position方法，设置底部轴移动到竖轴的位置
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# #设置坐标轴的范围
# ax.set_xlim(-1, 2)
# ax.set_ylim(-2, 3)
# #设置坐标轴的标签
# ax.set_xlabel('x_data')
# ax.set_ylabel('y_data')

#设置坐标轴的刻度显示的位置，top：显示在顶部，bottom：显示在底部，默认为none
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()