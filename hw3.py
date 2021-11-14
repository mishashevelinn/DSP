from skimage import color, data, restoration
from scipy.signal import convolve2d as conv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import fftconvolve

from skimage.feature import match_template


def blur(img, factor, plot=True):
    psf = np.ones((factor)) / factor
    psf = np.atleast_2d(psf)
    blured = conv2(astro, psf, 'same')
    if plot:
        fig, _ = plt.subplots()
        fig.suptitle(f'Convolved with {psf.shape[0]}X{psf.shape[1]} averager')
        plt.imshow(blured)
        plt.gray()
        plt.show()
    return blured


def deblur(img, h1=None, h2=None, a=None, b=None, c=None, plot=True):
    if h1 is None and h2 is None:
        h1 = np.array([1, -2, 1]) / 4
        h1 = np.atleast_2d(h1)
        h2 = h1.T
    if a is None and b is None and c is None:
        a, b, c = 1, 1, 1
    i1 = conv2(img * b, h1, 'same')
    i2 = img * a
    i3 = conv2(img * c, h2, 'same')
    deblurred = i1 + i2 + i3
    if plot:
        fig, _ = plt.subplots()
        fig.suptitle(f'Deblurred')
        plt.imshow(deblurred)
        plt.gray()
        plt.show()
    return deblurred


# astro = color.rgb2gray(data.astronaut())
# fig, ax = plt.subplots(1, 3)
# blurred = blur(astro, 3, plot=False)
# deblurred = deblur(blurred, plot=False)
# plt.gray()
# ax[0].imshow(astro)
# ax[1].imshow(blurred)
# ax[2].imshow(deblurred)
#
# plt.show()


a = np.zeros((10, 10))
a[1][2:3] = 1
a[1][3] = 1
a[2][2] = 1
a[2][7] = 1
a[3][7] = 1
a[3][8] = 1
a[6][1] = 1
a[6][2] = 1
a[6][6:9] = 1
a[7][2] = 1
a[7][6] = 1
a[7][8] = 1
a[8][6:9] = 1

pattern2 = np.zeros((3, 3))
pattern2[1][0:2] = 1
pattern2[2][1] = 1
pattern1 = np.ones((3, 3))*(-1) + pattern2
pattern1[1, 1] = 0
pat_sum = pattern1 + pattern2

print(pat_sum)

def pattern_match(img, pattern, mode='full'):
    plt.tight_layout()
    if isinstance(pattern, list):
        plt.gray()
        result = fftconvolve(img, pattern[0][::-1, ::-1],
                             mode=mode)[1:-1, 1:-1]
        fig, ax = plt.subplots(2, 3)
        ax[0][0].imshow(img)
        ax[0][1].imshow(pattern[0])
        ax[0][2].imshow(result)
        result2 = fftconvolve(img, pattern[1][::-1, ::-1],
                              mode=mode)[1:-1, 1:-1]
        ax[1][0].imshow(img)
        ax[1][1].imshow(pattern[1])
        ax[1][2].imshow(result2)
        plt.show()

        return result, result2

    else:
        plt.gray()
        result = fftconvolve(img, pattern[::-1, ::-1],
                             mode=mode)[1:-1, 1:-1]
        fig, ax = plt.subplots(1, 3)
        ax[0].imshow(img)
        ax[1].imshow(pattern)
        ax[2].imshow(result)
        plt.show()
        return result





h1, h2 = pattern_match(a, [pattern1, pattern2])
# plt.imshow(h1 - h2, cmap=plt.cm.gray)
# plt.show()

