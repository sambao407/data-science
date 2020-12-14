import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('datasets/Blurry/blurry_003.jpg')

#filter2D
kernel = np.ones((3,3),np.float32)/9
dst= dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()


#blur


