import cv2

img = cv2.imread('merge.jpg')
img2 = cv2.imread('5.jfif')

dis = cv2.subtract(img, img2)
# dist = cv2.subtract(dis, img2)
cv2.imshow('result', dis)
cv2.waitKey()
cv2.destroyAllWindows()