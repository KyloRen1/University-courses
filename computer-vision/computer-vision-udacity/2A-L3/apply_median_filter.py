import cv2
import numpy as np
from typing import List

# Helper function


def imnoise(img_in: List[int], method: str, dens: float) -> List[int]:

    if method == 'salt & pepper':
        img_out = np.copy(img_in)
        r, c = img_in.shape
        x = np.random.rand(r, c)
        ids = x < dens / 2.
        img_out[ids] = 0
        ids = dens / 2. <= x
        ids &= x < dens
        img_out[ids] = 255

        return img_out

    else:
        print("Method {} not yet implemented.".format(method))
        exit()


# Read an image
img = cv2.imread('images/moon.png', 0)
cv2.imshow('Image', img)

# TODO: Add salt & pepper noise
img_with_noise = imnoise(img, 'salt & pepper', 0.02)
cv2.imshow('Salt and pepper noise', img_with_noise)
# TODO: Apply a median filter. Use cv2.medianBlur
smoothed_img = cv2.medianBlur(img_with_noise, ksize=5)
cv2.imshow('Median Blur', smoothed_img)
cv2.waitKey(0)
