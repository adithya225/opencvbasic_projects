import cv2
import numpy as np

# apple=cv2.imread('apple.png')
# orange=cv2.imread('orange.png')
# print(apple.shape)
# print(orange.shape)
# apple_orange = np.hstack((apple[:,:256], orange[:,256:]))
#
#
# cv2.imshow('apple_orange',apple_orange)
# cv2.waitKey()
# cv2.destroyAllWindows()


Apple = cv2.imread('apple.png')
orange = cv2.imread('orange.png')

# generate Gaussian pyramid for A
G = Apple.copy()
print(G)
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = orange.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

lpA = [gpA[5]]
for i in range(6,0,-1):
    print(i)
    GE = cv2.pyrUp(gpA[i])
    GE=cv2.resize(GE,gpA[i - 1].shape[-2::-1])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B

lpB = [gpB[5]]
for i in range(6,0,-1):
    print(i)
    GE = cv2.pyrUp(gpB[i])
    GE = cv2.resize(GE, gpB[i - 1].shape[-2::-1])
    L = cv2.subtract(gpB[i-1],GE)
    print(L.shape)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
lpAc=[]
for i in range(len(lpA)):
    b=cv2.resize(lpA[i],lpB[i].shape[-2::-1])
    lpAc.append(b)
print(len(lpAc))
print(len(lpB))
j=0
for i in zip(lpAc,lpB):
    la,lb = i
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
    j=j+1
    LS.append(ls)

ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_= cv2.resize(ls_, LS[i].shape[-2::-1])
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
B= cv2.resize(orange, Apple.shape[-2::-1])
real = np.hstack((Apple[:,:cols//2],orange[:,cols//2:]))

cv2.imshow('blended', ls_)
cv2.imshow('real', real)
cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
cv2.waitKey()
cv2.destroyAllWindows()