import cv2

# Explore edge options

# Load an image
img = cv2.imread('images/fall-leaves.png')
cv2.imshow('Image', img)

# TODO: Create a Gaussian filter. Use cv2.getGaussianKernel.
gaussian_kernel = cv2.getGaussianKernel(ksize=5, sigma=3)
# TODO: Apply it, specifying an edge parameter (try different parameters).
# Use cv2.filter2D.
smoothed_img_border_const = cv2.filter2D(img, -1, gaussian_kernel,
                                         borderType=cv2.BORDER_CONSTANT)
cv2.imshow('Border Constant', smoothed_img_border_const)

smoothed_img_border_replicate = cv2.filter2D(img, -1, gaussian_kernel,
                                             borderType=cv2.BORDER_REPLICATE)
cv2.imshow('Border Replicate', smoothed_img_border_replicate)

smoothed_img_border_reflect = cv2.filter2D(img, -1, gaussian_kernel,
                                           borderType=cv2.BORDER_REFLECT)
cv2.imshow('Border Reflect', smoothed_img_border_reflect)

smoothed_img_border_reflect101 = cv2.filter2D(
    img, -1, gaussian_kernel, borderType=cv2.BORDER_REFLECT_101)
cv2.imshow('Border Reflect 101', smoothed_img_border_reflect101)

cv2.waitKey(0)
