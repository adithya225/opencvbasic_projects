import numpy as np
import cv2

img = cv2.imread('5.jfif')  #messy.jfif
img2 = cv2.imread('6.jfif')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b, g, r))

# ball = img[125:178, 148:213]
# img[90:0, 83:148] = ball

dist = cv2.add(img, img2)
cv2.imshow('image', dist)
cv2.imwrite('merge.jpg', dist)
cv2.waitKey(0)
cv2.destroyAllWindows()