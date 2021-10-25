import cv2 as cv
import numpy as np

camera = 0 # source of the video
video = cv.VideoCapture(camera)

# subtractor = cv.createBackgroundSubtractorMOG2(100, 50)

while True:
    ret, frame = video.read()

    # cv.imshow("Edge Detechtion", frame)

    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow("Laplacian", laplacian)

    edges = cv.Canny(frame, 150, 150)
    cv.imshow("Edges", edges)

    if cv.waitKey(5) == ord('X'):
        break
    

cv.destroyAllWindows()
video.release()