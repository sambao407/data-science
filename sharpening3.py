import numpy as np
import cv2 as cv

img = cv.imread('datasets/Blurry/blurry_095.jpg')
#img = cv.imread('datasets/Noisy/noisy_017.jpg')

blur = cv.GaussianBlur(img, (5, 5), 0)

kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])
dst = cv.filter2D(blur, -1, kernel)

window_name = 'image'
cv.imshow(window_name, dst)
cv.waitKey(0)

