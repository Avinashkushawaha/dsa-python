# import cv2
# import  cvzone
# cap = cv2.VideoCapture(0)
# cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# overlay = cv2.imread('native.png', cv2.IMREAD_UNCHANGED)
# while True:
#     _, frame = cap.read()
#     gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = cascade.detectMultiScale(gray_scale)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
#     cv2.imshow('Snap Dude', frame)
#     if cv2.waitKey(10) == ord('q'):
#                     break



import cv2
import cvzone

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)

# Load the pre-trained Haar Cascade for face detection
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the overlay image with an alpha channel
overlay = cv2.imread('native.png', cv2.IMREAD_UNCHANGED)

while True:
    # Capture each frame from the webcam
    _, frame = cap.read()
    
    # Convert the frame to grayscale for face detection
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = cascade.detectMultiScale(gray_scale, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        # Resize the overlay image to fit the detected face
        resized_overlay = cv2.resize(overlay, (w, h))
        
        # Overlay the resized image on the detected face area
        frame = cvzone.overlayPNG(frame, resized_overlay, [x, y])
    
    # Display the result
    cv2.imshow('Snap Dude', frame)
    
    # Break loop on pressing 'q'
    if cv2.waitKey(10) == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
