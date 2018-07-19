#%%
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
y = x**2

#%%
# Functional Method of creating a plot. use plt.show() if you are not using jupyter notebook extension.
plt.plot(x,y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('First Graph')

#%%
plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')

# Object oriented way of plotting graphs.
#%%
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel('X-Axis')
axes.set_ylabel('Y-Axis')
axes.set_title('My First Plot')

#%%
fig = plt.figure()
# Left , bottom , width and hieght is passed to create the axes in canvas.
# These values are actually percentages , so they should be beteween 0 and 1
axes1 = fig.add_axes([0.1,0.1,0.8,0.8]) 
axes2 = fig.add_axes([0.5,0.2,0.3,0.3])
axes1.plot(x,y)
axes1.set_title('Bigger Plot')
axes2.plot(y,x)
axes2.set_title('Smaller Plot')

#%%

# nrows and ncols basically tells you about how many plots you want to see.
# nrows is numer of rows and n cols is number of columns
# plt.subplots actually calls fig.add_axes() internally to crate axes.
x = np.linspace(0,5,11)
y = x**2
fig , axes = plt.subplots(nrows=2,ncols=2)
# axes returned by plt.subplots is just and np array with a list of axes objects.
# You can iterrate thru all of them and call lot for all of them.
# And since this is an array you can access each object based on its position in the array.
for current_ax in axes:
    for current_ax1 in current_ax:
        current_ax1.plot(x,y)
        current_ax1.set_xlabel('x-axis')

# tight_layout solves the over lapping of the plots. Use this at the end of plotting.
plt.tight_layout()

#%%
# FIGURE SIZE , ASPECT RATIO AND DPI
# figsize takes tuple with width and height of the figures in inches
# DPI is dots per inch or PIXEL per inch.
fig = plt.figure(figsize=(3,2))
fig.add_axes([0.1,0.1,0.8,0.8])

#%%
# figsize can also be used with subplots along with nrows and ncols parameters.
# 'r' is for red colour line
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
axes[0].plot(x,y,'r')
axes[1].plot(y,x,'b')
plt.tight_layout()

#%%
## Save a figure (png, jpg, pdf etc)
fig.savefig('SupportFiles/My_Pic.png',dpi=200)

#%%
# Legends: with lables we can use legends to identify the plots in single figure.
fig = plt.figure()
axes = fig.add_axes([0,0,1,1])
axes.plot(x,y, label='x and y')
axes.plot(y,x, label='y and x')
# adding legend is a 2 step process
# Before you can call axes.legend which just reference the string which you pass in axes.plot as label parameter.
axes.legend()
# If your legend box overlaps with your plot then you can specify loc parameter while calling axes.legend()
# loc parameter has a set of value which can be assigned to it. Look in documentaion for all possible values.
axes.legend(loc=0)
# Lets say none of these value works for you, you can provide a tuple to loc parameter specifiying the x and y value.
axes.legend(loc=(0.1,0.1))
