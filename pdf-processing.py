import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from google.colab.patches import cv_imshow

#read image
img = cv.imread('src.png', cv.IMREAD_GRAYSCALE)

#convert to binary
_ , bimg = cv.threshold(img, 200, 255, cv.THRESH_BINARY)

#extract edges
cimg = cv.Canny(bimg, 100, 200)

#detect lines
linesP = cv.HoughLinesP(cimg, 1, np.pi / 180, 50, None, 50, 10)

# Code verification is complete. I am able to generate the rho and theta for the horizontal and vertical lines. 
# The next step is to create simple and small functions that capture the code and simplify the implementation
# I will update the code after testing the fucntions.
