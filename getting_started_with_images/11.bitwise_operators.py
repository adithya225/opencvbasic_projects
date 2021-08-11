import cv2
import numpy as np

img1= np.zeros((400, 300, 3), np.uint8)
im1 = cv2.rectangle(img1, (200, 0), (100, 50),(255,255,255), -1)
img2 = cv2.imread("lena.png")
img2=cv2.resize(img2, (300,400))

print(img1.shape)
print(img2.shape)

bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img2, img1)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.waitKey(0)
cv2.destroyAllWindows()
