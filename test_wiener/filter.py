from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, restoration

img = Image.open('graph.png')
img = np.array(img)
img_gray = color.rgb2gray(img)

from scipy.signal import convolve2d as conv2
psf = np.ones((5, 5)) / 25
img_gray = conv2(img_gray, psf, 'full')

img_gray += 0.1 * img_gray.std() * np.random.standard_normal(img_gray.shape)

deconvolved, _ = restoration.unsupervised_wiener(img_gray, psf)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 5),
                       sharex=True, sharey=True)

plt.gray()

ax[0].imshow(img_gray, vmin=deconvolved.min(), vmax=deconvolved.max())
ax[0].axis('off')
ax[0].set_title('Data')

ax[1].imshow(deconvolved)
ax[1].axis('off')
ax[1].set_title('Self tuned restoration')

fig.tight_layout()

plt.show()
