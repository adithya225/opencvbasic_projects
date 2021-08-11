import cv2
import numpy as np
img=cv2.imread('')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('ul gp', layer)
lp = [layer]

for i in range(5, 0, -1):
    guassian_extended = cv2.pyrUp(gp[i])
    print('gp',guassian_extended.shape)
    print('i',gp[i-1].shape)
    laplacian = cv2.subtract(gp[i-1], guassian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('original image', img)

cv2.waitKey()
cv2.destroyAllWindows()