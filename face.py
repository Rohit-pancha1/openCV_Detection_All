import cv2
import os

# Absolute path to the haarcascade file
cascade_path = os.path.abspath("Resources/haarcascade_frontalface_default.xml")
if not os.path.exists(cascade_path):
    print(f"File not found: {cascade_path}")
    exit(1)

faceCascade = cv2.CascadeClassifier(cascade_path)

# Load the image
img = cv2.imread("data/face.png")

if img is None:
    print("Image not found. Check the path.")
else:
    # Convert the image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
    
    # Display the result
    cv2.imshow("Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
