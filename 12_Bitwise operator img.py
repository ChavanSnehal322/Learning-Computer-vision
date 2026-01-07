
#  Bitwise operator ( And, Or, Not, Exor)
#  remove the pixel 
#   on = 0
#  Off = 1

import cv2 as cv
import numpy as np



blank = np.zeros((400, 400), dtype = "int8")

rectangle = cv.rectangle( blank.copy(), (30, 30), (370, 370), 255, -1)

circle = cv.circle( blank.copy(), (200, 200), 200, 255, -1)

cv.imshow( ' Rectangle' , rectangle)
cv.imshow('Circle', circle)

#  Bitwise
#  1] AND
#  Takes two imges ( a, b) and returns a intersection of both images by placing one ( a on b ) on another

bitwise_And = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise_AND img', bitwise_And)

#  2] OR
#  Takes two imges ( a, b) and returns a intersection  & non intersection of both images by placing one ( b on a ) on another

bitwise_OR = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise OR img", bitwise_OR)

# 3] EXOR
# Takes two imges ( a, b) and returns a non intersection of both images by placing one ( a on b ) on another
bitwise_XOR = cv.bitwise_xor(rectangle, circle)
cv.imshow(" Bitwise XOR", bitwise_XOR)


# 4] NOT
#  Finds all the white pixels to convert it to black pixels in the image
bitwise_Not_rect = cv.bitwise_not(rectangle)
cv.imshow("Rectangle _Not ", bitwise_Not_rect)

bitwise_Not_circle = cv.bitwise_not(circle )
cv.imshow("Circle _Not ", bitwise_Not_circle)



#  Bitwise XOR - Bitwise OR = Bitwise AND
#  Bitwise AND - Bitwise OR = Bitwise XOR

cv.waitKey(0)