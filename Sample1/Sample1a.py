##############################
#####
##### This is sample code to load image (.jpg/png format) and display using open CV Window
##### import cv2 ---> import opencv package
##### import numpy as np ---> import numpy package as np object and we can use np in place of numpy with in this script
#####
##############################
##### Code Flow
#####
##### Step 1: Declare all the packages needed
#####
##### Step 2: "imread" is a function which is to read an image into an array
#####
##### Step 3: "imshow" is a function to display image array
#####
##### Step 4: waitKey(0) is used to read any key input, we wanted to close all the windows by pressing any key
#####
##### Step 5: "destroyAllWindows()" kills all the open windows created by openCV
#####
##############################

import cv2
import numpy as np
### Lena.jpg is obtained from https://bellard.org/bpg/lena.html
img = cv2.imread('lena.jpg',cv2.IMREAD_COLOR)

##Display image using OpenCV

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
