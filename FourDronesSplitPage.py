import cv2
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from split_image import split_image
import os
import CoordinateClick

def GothisPage():
    # to split the image into four segments
    window = tk.Tk()
    window.geometry("1920x1080")
    window.title("Four Drones")

    # go to coordinateClick window
    def goToCoordinateClick():
        window.destroy()
        CoordinateClick.CoordinatePicker()

    # read the image file directory
    def readAndimage():
        global filename
        fh = open('fileAddress.txt', 'r')
        filename = fh.readline()
        fh.close()

        file_split = 'image_split'
        # file does not exist then create
        if not os.path.exists(file_split):
            os.makedirs(file_split)
        # file exist then delete then make new file
        else:
            os.remove(file_split)
            os.makedirs(file_split)

        split_image(filename, 2, 2, False, False, False, file_split)
        col = 1  # start from column 1
        row = 3  # start from row 3
        # make loop to get image from image_split
        # double loop for grid 2x2

        f_types = [('Jpg Files', '*.jpg'),
                   ('PNG Files', '*.png')]  # type of files to select
        file_dir = tk.filedialog.askopenfilename(initialdir=file_split, multiple=True, filetypes=f_types)
        col = 1  # start from column 1
        row = 1  # start from row 3

        for images in file_dir:

            img = Image.open(images)
            img = img.resize((800, 800))
            img = ImageTk.PhotoImage(img)

            e1 = tk.Label(window)
            e1.grid(row=row, column=col,pady=30,padx=30)

            e1.image = img  # keep a reference by attaching it to a widget attribute
            e1['image'] = img  # Show Image
            # using pack() will make the interface messy

            if (col == 1 and row == 1):
                col = 2
            elif (col == 2 and row == 1):
                row = 2
                col = 1
            elif (col == 1 and row == 2):
                col = 2

    print("test")
    readAndimage()
    labelButton = tk.Button(window, text="pick the coordinates for the drone to fly through",
                            command=goToCoordinateClick)
    labelButton.grid(row=3, column=1)
    window.mainloop()

if __name__ == "__FourDronesSplitPage__":
    GothisPage()
