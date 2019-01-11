import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(1, (8, 5))
plt.scatter(x, y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.figure(2, (8, 5))
plt.plot(x, y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2 * x0 + 1
####plt.scatter画出来的是‘点’,参数s即size。
plt.scatter(x0, y0, s=50, color='b')
##plot([x0, y0], [x1, y1])————>画一条连接点x0到x1的线
##k--缩写：black，样式为--。lw：线的宽度
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

##method.1
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset point',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3'))
plt.show()