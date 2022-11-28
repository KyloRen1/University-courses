import cv2
import matplotlib.pyplot as plt
# Color planes

img = cv2.imread('images/fruit.png')
cv2.imshow("Fruit image", img)

print(img.shape)

# TODO: Select a color plane, display it, inspect values from a row
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Fruit image GRAY", img_gray)
print('1st row values: ', img_gray[0])

hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
print('Hist values: ', *hist)

cv2.waitKey(0)
