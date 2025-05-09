import cv2
import time
import glob
import os
from emailing import send_email
from threading import Thread

# Start video capture from default camera
video = cv2.VideoCapture(0)
time.sleep(1)  # Allow camera to warm up

first_frame = None  # Used to store the background frame for motion detection
status_list = []    # List to track motion status in consecutive frames
count = 1           # Counter for saving image files

def clean_folder():
    """Delete all png images in the images folder."""
    images = glob.glob("images/*png")
    for image in images:
        os.remove(image)

# Main loop for capturing and processing video frames
while True:
    status = 0  # Default status: no motion
    check, frame = video.read()  # Read a frame from the video stream

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur to reduce noise and improve motion detection
    gray_frame_gaussian = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Store the first frame to use as a baseline for detecting motion
    if first_frame is None:
        first_frame = gray_frame_gaussian

    # Compute the absolute difference between the first frame and current frame
    delta_frame = cv2.absdiff(first_frame, gray_frame_gaussian)

    # Apply a binary threshold to highlight differences (motion)
    thresh_frame = cv2.threshold(delta_frame, 45, 255, cv2.THRESH_BINARY)[1]
    # Dilate thresholded frame to fill in holes and emphasize moving regions
    dilate_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # Show the motion detection frame
    cv2.imshow("Capturing Video", dilate_frame)

    # Find contours of the moving areas
    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ignore small movements or noise
        if cv2.contourArea(contour) < 5000:
            continue
        # Get bounding box for the detected contour
        x, y, w, h = cv2.boundingRect(contour)
        # Draw a rectangle around the moving object
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        # If a rectangle is drawn, we detected motion
        if rectangle.any():
            status = 1  # Motion detected
            # Save the current frame as an image
            cv2.imwrite(f"images/{count}.png", frame)
            count += 1

            # Get a list of all captured images and select one from the middle
            all_images = glob.glob("images/*png")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]  # This image will be sent via email

    # Update the status list to keep track of last two motion states
    status_list.append(status)
    status_list = status_list[-2:]  # Keep only the last 2 values

    # If motion has just stopped (1 followed by 0), send email and clean folder
    if status_list[0] == 1 and status_list[1] == 0:
        email_thread = Thread(target=send_email, args=(image_with_object,))
        email_thread.daemon = True
        clean_folder_thread = Thread(target=clean_folder)
        clean_folder_thread.daemon = True

        # Start email sending in a separate thread
        email_thread.start()

    # Show the actual camera feed with rectangle (if any)
    cv2.imshow("Capturing Video", frame)

    # Press 'q' to quit the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Release video capture and start cleanup in a separate thread
video.release()
clean_folder_thread.start()
