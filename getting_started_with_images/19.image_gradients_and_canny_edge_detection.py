import cv2
import numpy as np
import matplotlib.pyplot as plt


img= cv2.imread('lena.png')
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelx= cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0 ,1)

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))
sobelcombine = cv2.bitwise_or(sobelx, sobely)

canny = cv2.Canny(img, 100, 250)
canny = np.uint8(np.absolute(canny))

titles=['image','laplacian','sobelx','sobely', 'scombine','canny']
images = [img, lap, sobelx, sobely, sobelcombine,canny]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()