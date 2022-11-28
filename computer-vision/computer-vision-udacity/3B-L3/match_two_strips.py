import cv2
import numpy as np
import matplotlib.pyplot as plt
from typing import List


# We will use the function implemented in the last quiz
# Find best match
def find_best_match(patch: List[float], strip: List[float]) -> int:
    # TODO: Find patch in strip and return column index (x value) of topleft corner
    # Paste your answer from the previous quiz here
    best_match = 0
    min_diff = float('inf')
    for i in range(strip.shape[1] - patch.shape[1]):
        curr_patch = strip[:, i: i + patch.shape[1]]
        diff = patch.ravel() - curr_patch.ravel()
        curr_diff = np.dot(diff, diff)
        if curr_diff < min_diff:
            min_diff = curr_diff
            best_match = i
    return best_match


def match_strips(
        strip_left: List[float],
        strip_right: List[float],
        b: int) -> List[int]:
    # For each non-overlapping patch/block of width b in the left strip,
    # find the best matching position (along X-axis) in the right strip.
    # Return a vector of disparities (left X-position - right X-position).
    # Note: Only consider whole blocks that fit within image bounds.
    res = []
    for i in range(0, strip_left.shape[1] - b, b):
        left_patch = strip_left[:, i: i + b]
        best_match = find_best_match(left_patch, strip_right)
        res.append(i - best_match)
    return np.array(res)

# Test code:


# Load images
left = cv2.imread('images/flowers-left.png')
right = cv2.imread('images/flowers-right.png')
cv2.imshow('Left', left)
cv2.imshow('Right', right)

# Convert to grayscale, double, [0, 1] range for easier computation
left_gray = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY) / 255.
right_gray = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY) / 255.

# Define strip row (y) and square block size (b)
y = 120
b = 100

# Extract strip from left image
strip_left = left_gray[y: y + b, :]
cv2.imshow('Strip Left', strip_left)

# Extract strip from right image
strip_right = right_gray[y: y + b, :]
cv2.imshow('Strip Right', strip_right)

# Now match these two strips to compute disparity values
disparity = match_strips(strip_left, strip_right, b)
print(disparity)

# Finally we plot the disparity values. Note that there may be some differences
# in the results shown in the quiz because we had to adapt the index values.
plt.plot(range(disparity.shape[0]), disparity)
plt.show()
plt.close('all')
