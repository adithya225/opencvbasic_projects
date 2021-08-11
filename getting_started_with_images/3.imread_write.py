import cv2

img = cv2.imread('lena.png', 1)   #'C:/Users/HP/OneDrive/Desktop/lena.jfif'

# 0 indicates black and white image
# 1 indicates colored image
# -1 indicates unchanged image, displays as it is.

cv2.imshow('result', img)
k=cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena1.png', img)
    cv2.destroyAllWindows()