'''
  File name: estimateAllTranslation.py
  Author:
  Date created:
'''

'''
  File clarification:
    Estimate the translation for all features for each bounding box as well as its four corners
    - Input startXs: all x coordinates for features wrt the first frame
    - Input startYs: all y coordinates for features wrt the first frame
    - Input img1: the first image frame
    - Input img2: the second image frame
    - Output newXs: all x coordinates for features wrt the second frame
    - Output newYs: all y coordinates for features wrt the second frame
'''

def estimateAllTranslation(startXs, startYs, img1, img2):
  #TODO: Your code here
  import scipy
  import numpy as np
  import cv2
  
  Ix=np.array([[-1,1],[-1,1]])
  Iy=np.array([[-1,-1],[1,1]])
  gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
  gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
  gradx1=scipy.signal.convolve2d(gray1,Ix,mode='same',boundary='symm')
  grady1=scipy.signal.convolve2d(gray1,Iy,mode='same',boundary='symm')
  gradx2=scipy.signal.convolve2d(gray2,Ix,mode='same',boundary='symm')
  grady2=scipy.signal.convolve2d(gray2,Iy,mode='same',boundary='symm')
  
  return gradx1,grady1
#  return newXs, newYs