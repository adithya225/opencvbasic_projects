import numpy as np
import cv2

img = cv2.imread('5.jfif')  #messy.jfif
img2 = cv2.imread('4.jpg')

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r = cv2.split(img)
img = cv2.merge((b, g, r))


img = cv2.resize(img, (400,300))
img2 = cv2.resize(img2,(400,300))

#dist = cv2.add(img, img2)
dist = cv2.addWeighted(img, 0.5, img2, 0.5, 0)
cv2.imshow('image', dist)
#cv2.imwrite('merge.jpg', dist)
cv2.waitKey(0)
cv2.destroyAllWindows()