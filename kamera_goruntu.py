import cv2

kamera= cv2.VideoCapture(0)

while True:
    ret, kare = kamera.read()

    cv2.imshow("kamera goruntusu", kare)


    if cv2.waitKey(1) != -1:
        break

kamera.release()
cv2.destroyAllWindows() 