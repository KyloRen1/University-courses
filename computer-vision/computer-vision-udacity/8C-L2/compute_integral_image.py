import cv2
import numpy as np
from typing import List


def compute_integral(img: List[float]) -> List[float]:
    # TODO: Compute I such that I(y,x) = sum of img(1,1) to img(y,x)

    #integral_matrix = np.zeros(img.shape)
    # for i in range(img.shape[0]):
    # 	for j in range(img.shape[1]):
    # 		integral_matrix[i][j] = np.sum(img[:i, :j])

    integral_matrix, _ = cv2.integral2(img)
    return integral_matrix


img = cv2.imread('images/dolphin.png', 0)
cv2.imshow("original_image", img)
print(img.shape)

# compute integral
img = np.float64(img)
I = compute_integral(img)
cv2.imshow("integral_image", (I / I.max()))

x1 = 150
y1 = 100
x2 = 350
y2 = 200

print("Sum: ", np.sum(img[y1:y2 + 1, x1:x2 + 1]))
print(I[y2, x2] - I[y1 - 1, x2] - I[y2, x1 - 1] + I[y1 - 1, x1 - 1])

cv2.waitKey(0)
