


#  Masking 
#  using bitwise operators to focus on specific objects in img ( faces, objects , to remove unwanted parts in the img)

import cv2 as cv
import numpy as np

#  Mask size should be same as that of the originl image

img = cv.imread('Reading a video Images/Photos/fullerton-california.jpeg')
cv.imshow('Banner', img)

#  blank should be same size as that of img
blank = np.zeros( img.shape[:2], dtype='uint8')
cv.imshow("Blank img", blank)

#  drawing circle over the blank img and masking it on the img
mask = cv.circle(blank, (img.shape[1]// 2, img.shape[0]// 2), 100, 255, -1)
cv.imshow("Masked", mask)

#  masked img
masked = cv.bitwise_and(img, img, mask = mask)
cv.imshow("Masked img", masked)


#  masked rect
mask_rect = cv.rectangle(blank.copy(), (img.shape[1]// 2, img.shape[0]// 2), (img.shape[1]// 2 + 150, img.shape[0] // 2 + 150), 250, -1 )
cv.imshow("Masked rect", mask_rect)


masked_rec = cv.bitwise_and(img, img, mask = mask_rect)
cv.imshow("Masked rec img", masked_rec)

cv.waitKey(0)