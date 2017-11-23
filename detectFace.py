'''
  File name: detectFace.py
  Author:
  Date created:
'''

'''
  File clarification:
    Detect or hand-label bounding box for all face regions
    - Input img: the first frame of video
    - Output bbox: the four corners of bounding boxes for all detected faces
'''

def detectFace(img):
  #TODO: Your code here
  import numpy as np
  import cv2 
  gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  face=face_cascade.detectMultiScale(gray,1.2,5)
#  for x,y,w,h in face:
#      cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#  cv2.imshow('fig 1',img)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
  bbox=np.zeros((len(face),4,2))
  for i in range(len(face)):
     bbox[i,:,0]=np.array([face[i,0],face[i,0]+face[i,2],face[i,0]+face[i,2],face[i,0]])
     bbox[i,:,1]=np.array([face[i,1],face[i,1],face[i,1]+face[i,3],face[i,1]+face[i,3]])
  
  return bbox