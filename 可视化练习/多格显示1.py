import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])   #第一个为x的集合，第二个为y的集合
##plot连接点(0,0)和(1,1)画线

plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 3)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 4)
plt.plot([0, 1], [0, 1])
plt.show()