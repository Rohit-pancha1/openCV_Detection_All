import cv2
# print("Package Imported")

# img = cv2.imread("data/photo.png")

# if img is None:
#     print("Image not found. Check the path.")
# else:
#     cv2.imshow("Output", img)
#     cv2.waitKey(0)  # Use 0 to wait indefinitely until a key is pressed
#     cv2.destroyAllWindows()


cap = cv2.VideoCapture("data/accident.mp4")
# cap = cv2.VideoCapture(1)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame from video stream")
        break
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
