# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:12:38 2019

@author: Michael
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import scipy.interpolate as si
import scipy.constants as sc
import scipy.optimize as so

x=st.norm.rvs(loc=0, scale=.05, size=1000)
px=st.norm.rvs(loc=0, scale=0.3, size=1000)
fig=plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Move left y-axis and bottim x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks([1])
ax.xaxis.set_ticklabels(['px'])

ax.yaxis.set_ticks([1])
ax.yaxis.set_ticklabels(['x'])

plt.scatter(x,px,s=0.9,alpha=0.2)
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.show()

