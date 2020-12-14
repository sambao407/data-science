import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import imageio

img = imageio.imread('datasets/Blurry/blurry_001.jpg')

#filter2D
#kernel = np.ones((3,3),np.float32)/9
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
dst= dst = cv.filter2D(img,-1,kernel)

fig, axes = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True, figsize=(15, 15))
axes = axes.ravel()
axes[0].imshow(img)
axes[1].imshow(dst)
for ax in axes:
    ax.axis('off')
fig.tight_layout()
plt.show()

"""window_name = 'Sharpened image'
cv.imshow(window_name,dst)
cv.waitKey(0)"""

#blur


