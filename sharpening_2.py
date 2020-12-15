import scipy
import numpy
from scipy import ndimage
import imageio
import matplotlib.pyplot as plt

blurryPath = 'datasets/Blurry/'
im = imageio.imread(blurryPath + 'blurry_150.jpg')/255
im_blurred = ndimage.gaussian_filter(im, (5,5,0))
im_detail = numpy.clip(im - im_blurred, 0, 1)

fig, axes = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True, figsize=(15, 15))
axes = axes.ravel()
axes[0].imshow(im)
axes[0].set_title('Original image', size=15)
axes[1].imshow(im_blurred)
axes[1].set_title('Blurred image, sigma=5', size=15)
axes[2].imshow(im_detail)
axes[2].set_title('Detail image', size=15)
alpha = [1, 2, 3]
for i in range(3):
    im_sharp = numpy.clip(im + alpha[i]*im_detail, 0, 1)
    axes[3+i].imshow(im_sharp)
    axes[3+i].set_title('Sharpened image, alpha=' + str(alpha[i]), size=15)
for ax in axes:
    ax.axis('off')
fig.tight_layout()
plt.show()