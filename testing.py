# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:19:06 2017

@author: zoue
"""
import numpy as np 
import scipy 


col=10
row=9
x=np.linspace(0,4,5)
y=np.linspace(0,4,5)
z=np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[0,0,0,0,0]])

xv, yv = np.meshgrid(x, y, sparse=False, indexing='xy')

interF= scipy.interpolate.interp2d(xv, yv, z, kind='linear')
start=10
print np.arange(start-5,start+5,1)