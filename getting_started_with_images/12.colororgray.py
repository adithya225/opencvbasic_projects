import numpy as np
import cv2 as cv

def nothing(x):
    pass



cv.namedWindow("image")

cv.createTrackbar('CP', 'image', 0, 400, nothing)


switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)


while(1):
    img = cv.imread('lena.png')
    pos = cv.getTrackbarPos('CP', 'image')
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50,150), font, 4, (0,0,255), 5)


    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("image", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
