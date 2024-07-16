import cv2
import numpy as np

img = cv2.imread("data/flower.png")

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))


if img is None:
    print("Image not found. Check the path.")
else:
    cv2.imshow("Horizonatal", imgHor)
    cv2.imshow("Vertical", imgVer)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()