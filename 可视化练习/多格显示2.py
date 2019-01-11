import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 1:subplot2grid
########################
plt.figure(1)
## (3,3)为格子的排列，(0,0)为此时的坐标系的起点格子，colspan=3：该坐标系的列跨度为3格
## rowspan=1：该坐标系的行跨度为1格
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
###在该坐标系上画曲线
ax1.plot([1,2], [1, 2])
ax1.set_title('fuc 1')
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))

## method 2:gridspec
##### [a:b,c]所表示的范围：a-->b-1,即不包括b。
plt.figure(2)
gs = gridspec.GridSpec(3, 3)
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])

## method 3:easy to define structure                            ##sharex 共享x轴
## f即输出的画布。
f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])
plt.show()