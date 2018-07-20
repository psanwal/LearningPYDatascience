#%%
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2
fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])
ax1.set_title('title')
ax1.set_xlabel('x')
ax1.set_xlabel('y')
ax1.plot(x,y)
ax2.plot(x,y)

#%%
#[0,0,1,1] and [0.2,0.5,.4,.4]
fig = plt.figure()
ax3 = fig.add_axes([0,0,1,1])
ax4 = fig.add_axes([0.2,0.5,.4,.4])
ax3.set_xlim([0,100])
ax3.set_ylim([0,10000])
ax4.set_xlim([20,22])
ax4.set_xlim([30,50])
ax3.set_xlabel('X')
ax3.set_ylabel('Z')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_title('ZOOM')
ax3.plot(x,z)
ax4.plot(x,y)

#%%
fig , axes = plt.subplots(nrows=1, ncols=2, figsize=(8,2))
axes[0].plot(x,y, color='blue', linestyle='--', linewidth=2)
axes[1].plot(x,z, color='Red', linewidth=3)

