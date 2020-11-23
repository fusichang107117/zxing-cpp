#!/usr/bin/python
# -*- coding: UTF-8 -*-


import cv2

# opencv读取图像
img = cv2.imread('./out1.png', 1)

#print(img.shape)
#print(img.dtype)

#cv2.imshow('img', img)

#iCopy = copy.deepcopy(img)

#gray = cv2.cvtColor(iCopy, cv2.COLOR_BGR2GRAY)

#print(gray.shape)
#print(gray.dtype)

#cv2.imshow('gray', gray)

#img_shape = img.shape  # 图像大小(565, 650, 3)
#h = img_shape[0]
#w = img_shape[1]
# 最大图像灰度值减去原图像，即可得到反转的图像
dst = 255 - img

#dst = img
#cv2.imshow('dst', dst)

#cv2.imwrite('1.png',gray)

cv2.imwrite('2.png',dst)

#cv2.destroyAllWindows()

#cv2.waitKey()
