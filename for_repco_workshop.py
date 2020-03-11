## Created 11 Nov 2019

import numpy as np
import matplotlib.pyplot as plt
import pickle 
from numpy import *
import scipy.linalg
import pandas as pd 
import netCDF4 as nc4
import xarray as xr
from scipy.stats.stats import pearsonr

""" Loading Mikael's sinking data """

fileObject = open('./data/raw/forDelphine.pickle', 'rb')
data = pickle.load(fileObject)
lons = pickle.load(fileObject) # longitude coordinates
lats = pickle.load(fileObject) # latitude

""" Winter 2007 """ # 1st data point = Feb 2006
w07 = 0+12
w07_data0 = data[w07,:,:]
w07_data = (w07_data0- np.min(w07_data0))/(np.max(w07_data0)-np.min(w07_data0)) # To normalise the data between 0 and 1

""" Spring 2007 """
sp07 = 0+15
sp07_data0 = data[sp07,:,:]
sp07_data = (sp07_data0- np.min(sp07_data0))/(np.max(sp07_data0)-np.min(sp07_data0))

""" Summer 2007 """
su07 = 0+18
su07_data0 = data[su07,:,:]
su07_data = (su07_data0- np.min(su07_data0))/(np.max(su07_data0)-np.min(su07_data0))

""" Autumn 2007 """
a07 = 0+21
a07_data0 = data[a07,:,:]
a07_data = (a07_data0- np.min(a07_data0))/(np.max(a07_data0)-np.min(a07_data0))

X, Y = np.meshgrid(lons,lats)


med_lon_min = min(lons)
med_lon_max = max(lons)
med_lat_min = min(lats)
med_lat_max = max(lats)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
ax1.scatter(X,Y,w07_data.T,c=w07_data.T,cmap=plt.cm.jet,vmin=0, vmax=0.2) #row=0, col=0
ax1.title.set_text('Jan \'07')
ax2.scatter(X,Y,sp07_data.T,c=sp07_data.T,cmap=plt.cm.jet,vmin=0, vmax=0.2) #row=1, col=0
ax2.title.set_text('April \'07')
ax3.scatter(X,Y,su07_data.T,c=su07_data.T,cmap=plt.cm.jet,vmin=0, vmax=0.2) #row=0, col=1
ax3.title.set_text('July \'07')
ax4.scatter(X,Y,a07_data.T,c=a07_data.T,cmap=plt.cm.jet,vmin=0, vmax=0.2) #row=1, col=1
ax4.title.set_text('Oct \'07')
#ax.colorbar(ax4)
fig.suptitle('Sinking')
plt.show()
plt.savefig('./results/figures/Sinking_2007.png')
