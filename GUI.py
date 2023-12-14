import tkinter as tk
from tkinter import filedialog
import os

import cv2
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
    start_x = int(x / 3)
    if y - h > 60:
        h = y + 50
    if x - w > 60:
        w = x + 50
    cropped_face = image[30:(h + y + 150), start_x:int((w + x) + 100)]
    dim = (400, 600)
    resized = cv2.resize(cropped_face, dim, interpolation=cv2.INTER_AREA)

    # Save the cropped face to the output path
    cv2.imwrite(output_path, resized)


class FolderBrowserApp:
    folder_path=None
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Browser App")

        self.create_widgets()

    def create_widgets(self):
        # Entry for displaying the selected folder
        self.folder_entry = tk.Entry(self.root, width=80)
        self.folder_entry.pack(pady=10)

        # Button to open the file dialog
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_folder)
        self.browse_button.pack(pady=10)

        self.start_processing = tk.Button(self.root, text="Start Processing", command=self.get_files)
        self.start_processing.pack(pady=10)


    def browse_folder(self):
        # Open the file dialog to select a folder
        folder_path = filedialog.askdirectory()

        # Update the Entry widget with the selected folder path
        if folder_path:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_path)
            self.folder_path=folder_path
        # print(self.folder_entry)
        #     self.get_files(folder_path)

    def get_files(self):
        import filetype
        # from  main import crop_face
        if self.folder_path:
            print(os.listdir(self.folder_path))
            output=f"{self.folder_path}/output"
            # if os.path.exists(output):
            #     os.rmdir(output)
            # os.makedirs(output)
            os.chdir(output)

            for filename in os.listdir(self.folder_path):
                try:
                    if filetype.is_image(f"{self.folder_path}/{filename}"):
                        # print(f"{filename} is a valid image...")
                        output_face_path = f"{output}/{filename}"
                        crop_face(f"{self.folder_path}/{filename}",output_face_path)

                except:
                    pass
                    # print(f"{filename} is a valid video...")


if __name__ == "__main__":
    root = tk.Tk()
    app = FolderBrowserApp(root)
    root.geometry("550x150")
    root.mainloop()




