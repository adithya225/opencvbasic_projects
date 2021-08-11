import cv2
#import matplotlib.pyplot as plt   # or you can give from matplotlib import pyplot as plt

# img = cv2.imread('lena.png')
# cv2.imshow('image', img)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
# plt.imshow(img)
# plt.xticks([]), plt.yticks([])     # used to hide the x axis and y axis notations
# plt.show()
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# either above program or you can view the down one for verifying this project
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("gradient.jfif")

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ["original", 'bianry', 'inv', ' trunc', 'zero', 'zero_inv']
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(3,2,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# cv2.imshow("image", img)
# cv2.imshow("th1", th1)
# cv2.imshow("th2", th2)
# cv2.imshow("th3", th3)
# cv2.imshow("th4", th4)
# cv2.imshow("th5", th5)
plt.show()
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()
