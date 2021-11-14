import numpy as np


from skimage import data, img_as_float
from skimage import exposure

img1 = np.array([1, 2, 3, 4, 7, 6])

img2 = np.array([3, 4, 1, 5, 7, 3])
alpha = 1
beta = 2


def tri_median(data):

    res = []
    for i in range(len(data) - 2):
        res.append(np.median(np.array(data[i:i + 3])))
    return np.array(res)


H = lambda data: tri_median(data)


def test_linearity():
    print(f'alpha * H(img1) = {alpha * H(img1)}')
    print(f'beta * H(img2) = {beta * H(img2)}')
    print(f'now sum them: {alpha * H(img1) + beta * H(img2)}')
    print(f'H(alpha * img1 + beta * img2) = {H(alpha * img1 + beta * img2)}')
    assert (alpha * H(img1) + beta * H(img2) == H(alpha * img1 + beta * img2)).all()


def test_spatial_invariance():
    shifted_input = np.roll(img1, alpha, axis=0)
    print(f'H(img(x - alpha) = {H(shifted_input)}')
    print(f'H(img)(x - alpha) = {np.roll(H(img1), alpha)}')
    assert (H(shifted_input) == np.roll(H(img1), alpha)).all()





