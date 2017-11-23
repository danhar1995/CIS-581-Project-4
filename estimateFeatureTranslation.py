'''
  File name: estimateFeatureTranslation.py
  Author:
  Date created:
'''

'''
  File clarification:
    Estimate the translation for single features 
    - Input startX: the x coordinate for single feature wrt the first frame
    - Input startY: the y coordinate for single feature wrt the first frame
    - Input Ix: the gradient along the x direction
    - Input Iy: the gradient along the y direction
    - Input img1: the first image frame
    - Input img2: the second image frame
    - Output newX: the x coordinate for the feature wrt the second frame
    - Output newY: the y coordinate for the feature wrt the second frame
'''

def estimateFeatureTranslation(startX, startY, Ix, Iy, img1, img2):
  #TODO: Your code here
  import numpy as np
  import scipy
  It=img2-img1
  It=It[startY-5:startY+5,startX-5:startX+5]
  Ix=Ix[startY-5:startY+5,startX-5:startX+5]
  Iy=Iy[startY-5:startY+5,startX-5:startX+5]
  [row,col]=np.asarray(img1.shape)
  xlin=np.arange(startX-5,startX+5,1)
  ylin=np.arange(startY-5,startY+5,1)
  xv, yv = np.meshgrid(xlin, ylin, sparse=False, indexing='xy')
  interFIx=scipy.interpolate.interp2d(xv, yv, Ix, kind='linear')
  interFIy=scipy.interpolate.interp2d(xv, yv, Iy, kind='linear')
  interFIt=scipy.interpolate.interp2d(xv, yv, It, kind='linear')
  
  
  newX=startX+2
  newY=startY+2
  return newX, newY