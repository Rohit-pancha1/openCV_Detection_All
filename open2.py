import cv2
import numpy as np

img = cv2.imread("data/ertiga.png")
print(img.shape)



imgResize = cv2.resize(img,(300, 200))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]

if img is None:
    print("Image not found. Check the path.")
else:
    cv2.imshow("Image", img)
    cv2.imshow("Image Resize", imgResize)
    cv2.imshow("Image Cropped", imgCropped)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
