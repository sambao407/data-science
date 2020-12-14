import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('datasets/Blurry/blurry_001.jpg')

#filter2D
#kernel = np.ones((3,3),np.float32)/9
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
dst= dst = cv.filter2D(img,-1,kernel)
window_name = 'image'
cv.imshow(window_name,dst)
cv.waitKey(0)


#blur


