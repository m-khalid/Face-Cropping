import cv2

def crop_human(image_path):
    # Load the pre-trained HOG detector for human detection
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # Load the image
    image = cv2.imread(image_path)

    # Resize the image for faster processing (optional)
    image = cv2.resize(image, (640, 480))

    # Detect humans in the image
    humans, _ = hog.detectMultiScale(image)

    # Crop and save the first detected human (if any)
    if len(humans) > 0:
        x, y, w, h = humans[0]  # Assuming the first detection is the human
        cropped_human = image[y:y+h, x:x+w]

        # Display the cropped human
        cv2.imshow("Cropped Human", cropped_human)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the cropped



crop_human("1.png")