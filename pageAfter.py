from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image



def startPage():
    # create window
    root1 = tk.Tk()
    root1.geometry("1920x1080")
    root1.title("Image Upload")
    root1.config(bg="#204050")

    # Load the image
    image23 = Image.open("bgother.png")
    background_image1 = ImageTk.PhotoImage(image23)

    # Create a Label widget with the image
    background_label = tk.Label(root1, image=background_image1)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # choose file function and resized the image
    def openFile():
        global image_used
        f_types = [('Jpg Files', '*.jpg'), ('PNG Files', '*.png')]
        image_used = filedialog.askopenfilename(filetypes=f_types)
        imgForpg2 = Image.open(image_used)
        imgForpg2_resized = imgForpg2.resize((800, 800), Image.ANTIALIAS)
        imgForpg2 = ImageTk.PhotoImage(imgForpg2_resized)
        my_label = tk.Label(root1)
        my_label.grid(row=3, column=2,columnspan=3)
        my_label.image = imgForpg2
        my_label['image'] = imgForpg2
        fh = open('fileAddress.txt', 'w')
        fh.write(image_used)
        fh.close()
        label = tk.Label(root1, text="Image is displayed", bg="#204050", borderwidth=4,font=("Arial", 34),fg="#FFFFFF")
        label.grid(row=1, column=2)
        Button4Drones = tk.Button(root1, text="4 Drones", command=FDronePage).place(x=600, y=50)

        Button2Drones = tk.Button(root1, text="2 Drones", command=TDronePage).place(x=700, y=50)

    # if want four drones then do this function
    def FDronePage():
        root1.destroy()
        from split_image import split_image
        import os
        import CoordinateClick

        def GothisPage():
            # to split the image into four segments
            window = tk.Tk()
            window.geometry("1920x1080")
            window.title("Four Drones")

            # Load the image
            imagebg = Image.open("bgother.png")
            background_imagebg = ImageTk.PhotoImage(imagebg)

            # Create a Label widget with the image
            background_label1 = tk.Label(window, image=background_imagebg)
            background_label1.place(x=0, y=0, relwidth=1, relheight=1)

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

                file_split = r'C:\Users\muhdm\PycharmProjects\pythonProject1\image_split'
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
                    img = img.resize((650, 450))
                    img = ImageTk.PhotoImage(img)

                    e1 = tk.Label(window)
                    e1.grid(row=row, column=col)

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
                                    command=goToCoordinateClick,
                                    )
            labelButton.grid(row=3, column=1,columnspan=2)
            window.columnconfigure(0, weight=1)
            window.columnconfigure(1, weight=0)  # Empty column with weight 0
            window.columnconfigure(2, weight=0)
            window.columnconfigure(3, weight=1)
            window.mainloop()

        GothisPage()
    # if want two drones then do this function
    def TDronePage():
        root1.destroy()
        from split_image import split_image
        import os
        import CoordinateClick2

        def GothisPage():
            # to split the image into four segments
            window = tk.Tk()
            window.geometry("1920x1080")
            window.title("Two Drones")

            imagebg = Image.open("bgother.png")
            background_imagebg = ImageTk.PhotoImage(imagebg)

            # Create a Label widget with the image
            background_label1 = tk.Label(window, image=background_imagebg)
            background_label1.place(x=0, y=0, relwidth=1, relheight=1)

            # go to coordinateClick window
            def goToCoordinateClick():
                window.destroy()
                CoordinateClick2.CoordinatePicker()

            # read the image file directory
            def readAndimage():
                global filename
                fh = open('fileAddress.txt', 'r')
                filename = fh.readline()
                fh.close()

                file_split = r'C:\Users\muhdm\PycharmProjects\pythonProject1\image_split'
                # file does not exist then create
                if not os.path.exists(file_split):
                    os.makedirs(file_split)
                # file exist then delete then make new file
                else:
                    os.remove(file_split)
                    os.makedirs(file_split)

                split_image(filename, 1, 2, False, False, False, file_split)
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
                    img = img.resize((650, 450))
                    img = ImageTk.PhotoImage(img)

                    e1 = tk.Label(window)
                    e1.grid(row=row, column=col)

                    e1.image = img  # keep a reference by attaching it to a widget attribute
                    e1['image'] = img  # Show Image
                    # using pack() will make the interface messy


                    col = 2


            print("test")
            readAndimage()
            labelButton = tk.Button(window, text="pick the coordinates for the drone to fly through",
                                    command=goToCoordinateClick,
                                    )
            labelButton.grid(row=3, column=1, columnspan=2)

            window.columnconfigure(0, weight=1)
            window.columnconfigure(1, weight=0)  # Empty column with weight 0
            window.columnconfigure(2, weight=0)
            window.columnconfigure(3, weight=1)
            window.rowconfigure(0, weight=1)
            window.rowconfigure(1, weight=0)  # Empty row with weight 0
            window.rowconfigure(2, weight=0)
            window.rowconfigure(3, weight=0)
            window.rowconfigure(4, weight=1)
            window.mainloop()

        GothisPage()

    # upload button image
    btu = Image.open("upload.png")
    resized_image_up = btu.resize((50, 50), Image.ANTIALIAS)
    new_image_upload = ImageTk.PhotoImage(resized_image_up)

    global label
    # using grid from tkinter,pack() sometimes not show image
    labelButton = tk.Button(root1, image=new_image_upload, command=lambda: openFile(), borderwidth=2, bg="#FFFFFF",
                            border=3,padx=30, pady=10)
    labelButton.place(x=1200, y=10)
    label = tk.Label(root1, text="Please Upload File", bg="#204050", borderwidth=4,font=("Arial", 34),padx=30, pady=10,fg="#FFFFFF")
    label.grid(row=1, column=2)
    root1.columnconfigure(0, weight=0)
    root1.columnconfigure(1, weight=0)  # Empty column with weight 0
    root1.columnconfigure(2, weight=1)

    root1.mainloop()


if __name__ == "__pageAfter__":
    startPage()










