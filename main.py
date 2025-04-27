import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1) # Allow camera to warm up
first_frame = None 

while True:
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_fram_gaussian = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_fram_gaussian
    
    delta_frame = cv2.absdiff(first_frame, gray_fram_gaussian)

    thresh_frame = cv2.threshold(delta_frame, 45, 255, cv2.THRESH_BINARY)[1]
    dilate_frame = cv2.dilate(thresh_frame, None, iterations=2)
    cv2.imshow("Capturing Video", dilate_frame)

    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
    cv2.imshow("Capturing Video", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
