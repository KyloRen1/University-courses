import cv2
import numpy as np


# For Your Eyes Only
frizzy = cv2.imread('images/frizzy.png')
froomer = cv2.imread('images/froomer.png')
cv2.imshow('Frizzy', frizzy)
cv2.imshow('Froomer', froomer)


# TODO: Find edges in frizzy and froomer images
frizzy_canny = cv2.Canny(frizzy, 100, 200)
froomer_canny = cv2.Canny(froomer, 100, 200)

# TODO: Display common edge pixels
common_edges = np.logical_and(frizzy_canny, froomer_canny).astype(np.uint8)
cv2.imshow('Common edges', common_edges * 255.)
cv2.waitKey(0)
