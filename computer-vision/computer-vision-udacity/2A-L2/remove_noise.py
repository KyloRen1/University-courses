import cv2
import numpy as np
from typing import List

# Apply a Gaussian filter to remove noise
img = cv2.imread('images/saturn.png')
cv2.imshow('Img', img)

# TODO: Add noise to the image


def add_noise(
        img: List[int],
        mean: float = 1.0,
        std: float = 0.5) -> List[int]:
    noise = np.random.normal(mean, std, img.shape)
    img_with_noise = img + noise
    return img_with_noise.astype(np.uint8)


img_with_noise = add_noise(img, mean=10., std=5.)
cv2.imshow('Saturn image with noise', img_with_noise)

# TODO: Now apply a Gaussian filter to smooth out the noise


def apply_gaussian_filter(img: List[int], kernel_size: int = 5) -> List[int]:
    res = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    return res.astype(np.uint8)


img_smoothed = apply_gaussian_filter(img_with_noise)
cv2.imshow('Saturn smoothed image', img_smoothed)
cv2.waitKey(0)
