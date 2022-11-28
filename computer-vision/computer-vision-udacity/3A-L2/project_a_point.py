import cv2
import numpy as np
from typing import List

# Project a point from 3D to 2D using a matrix operation

# Given: Point p in 3-space [x y z], and focal length f
# Return: Location of projected point on 2D image plane [u v]


def project_point(p: List[float], f: float) -> List[float]:
    # TODO: Define and apply projection matrix
    projection_matrix = np.array(
        [[f, 0, 0, 0],
         [0, f, 0, 0],
         [0, 0, 1, 0]]
    )
    p = np.append(p, 1).transpose()
    projection = np.dot(projection_matrix, p)
    return [projection[0] / projection[2], projection[1] / projection[2]]


# Test: Given point and focal length (units: mm)
p = np.array([[200, 100, 100]])
f = 50

print(project_point(p, f))
