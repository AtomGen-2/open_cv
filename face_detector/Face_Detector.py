# import the library opencv
# OPENCV is a open source computer vision librabry maintained by the people, which contains a lot of pre trained data sets
import cv2
import random
# load some pre-trained data on face frontals from opencv (haar cascade algorithms)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Classifier basically means a detector. It is an object that can detect or classify stuff as a face or not.
# Choose an image to detect face in (imread = imageRead)
# images are basically an array of numbers [pixels are reporesented as numbers]
# img = cv2.imread('rdj.jpg')
# img = cv2.imread('2 faces.jpg')
# webcam = cv2.VideoCapture(0=default camera capture // 'video.mp4')
webcam = cv2.VideoCapture(0)
# iterate forever, till the video ends or we kill the webcam
while True: 
    # read current frame
    # successful_frame_read is just a boolean which tells us whether or not reading was successful, the actual data is stored in frame
    successful_frame_read, frame = webcam.read()
# we need to convert images into grayscale, because thats the only way with which you can identify images in opencv { not in color }
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('FaceDetector', grayscaled_frame)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)
    numberoffaces = len(face_coordinates)
    print(numberoffaces)
    for i in range(0, numberoffaces):
        (x, y, w, h) = face_coordinates[i]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (random.randrange(128, 256), random.randrange(128, 256), random.randrange(128, 256)), 2)
    cv2.imshow('Webcam Enabled', frame)
    # the image loads and immediatly closes. We do not want that, so we use the "cv2.waitKey()" to ensure that the image stays and waits until we press a key.
    # we are specifiing a number in the parenthesis, which signifis that it will wait for 1ms before auto-hitting a key, allowing you to capture multiple frames.
    key = cv2.waitKey(1)
    # to avoid force quiting each time, stop if Q is pressed, asci character of Q and q is 81 and 113
    if key == 81 or key == 113:
        break
# release the VideoCapture Object
webcam.release()

""" # Detect faces, irrespective of the scale(MultiScale)
# This gives us the coordinates of the face, so that we can form a rectangle around it.
# [[35 74 420 420]] first 2 numbers are coordinates of upper left point, second 2 are the width and height pf the square formed
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
face_coordinates = trained_face_data.detectMultiScale(grayscaled_frame)

# Draw a rectangle around the face 
# cv2.rectangle(image, (xy coordinate of upper left point), (xy coordinate of bottom right + xy coordinate of upper left), (b, g , r for rectangle), (thickness of rectangle))
numberoffaces = len(face_coordinates)
print(numberoffaces)
for i in range(0, numberoffaces):
    (x, y, w, h) = face_coordinates[i]
    cv2.rectangle(img, (x, y), (x + w, y + h), (random.randrange(128, 256), random.randrange(128, 256), random.randrange(128, 256)), 2)
# cv2.rectangle(img, (35, 74), (420 + 35, 420 + 74), (0, 255, 0), 2)
# cv2.imshow('name you want to be displayed in loaded image', img)
cv2.imshow('FaceDetector', img)
# the image loads and immediatly closes. We do not want that, so we use the "cv2.waitKey()" to ensure that the image stays and waits until we press a key.
cv2.waitKey() """

# print("Code Completed")
