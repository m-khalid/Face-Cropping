from builtins import print

import cv2
from PIL import Image
from numpy import inexact


def crop_face(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # dim = (300, 600)
    dim = (554, 604)

    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the pre-trained face detector from OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Detect faces in the image
    # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=0)

    # Check if any faces are detected
    if len(faces) == 0:
        print("No faces found in the image.")
        cv2.imwrite(output_path, image)
        return
    x, y, w, h = faces[0]
    start_x=int(x/3)
    if y-h>60:
        h=y+50
    if x - w > 60:
        w = x + 50
    cropped_face = image[30:(h+y+150), start_x:int((w+x)+100)]
    dim = (400, 600)
    resized = cv2.resize(cropped_face, dim, interpolation=cv2.INTER_AREA)

    # Save the cropped face to the output path
    cv2.imwrite(output_path, resized)
