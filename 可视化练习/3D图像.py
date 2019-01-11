import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#创建3D图形对象
fig = plt.figure()  #创建画布
ax = Axes3D(fig)

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
# print(X)
# print(Y)
X,Y = np.meshgrid(X, Y)    #构造网格矩阵。
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)
#输出3D图像  rstride：行跨度;cstride：列跨度
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
#zdir：将哪个方向进行投射, offset:投射到Z=-2的位置
ax.contour(X, Y, Z, zdir='Z', offset=-2, camp='rainbow')

ax.set_zlim(-2, 2)
plt.show()