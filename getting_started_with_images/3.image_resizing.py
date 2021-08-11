import cv2
import numpy as np

img = cv2.imread('a-c.jfif')
apple = cv2.resize(img,(512,512))

cv2.imwrite('apple.png', apple)

print(apple.shape)
cv2.imshow('out',apple)
cv2.waitKey()
cv2.destroyAllWindows()