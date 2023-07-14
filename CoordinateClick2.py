# importing the module
import cv2
import os
import glob
from tkinter import messagebox
import Calculate_distance_matrix_2Drones  as cal




def CoordinatePicker():
    cord = list()

    def show_popup():
        messagebox.showinfo("Info", "Press any button after choosing the coordinates")
    show_popup()

    # function to display timport PySimpleGUIhe coordinates of
    # of the points clicked on the image
    def click_event(event, x, y, flags, params):
        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:
            # displaying the coordinates
            # on the Shell
            print(x, ' ', y)
            cordtxt = str(x) + " " + str(y)
            print(cordtxt)
            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, '.', (x, y), font,
                        1, (255, 0, 0), 2)
            cv2.imshow('image', img)
            cord.append(cordtxt)

        # checking for right mouse clicks
        if event == cv2.EVENT_RBUTTONDOWN:
            # displaying the coordinates
            # on the Shell
            print(x, ' ', y)

            # displaying the coordinates
            # on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            b = img[y, x, 0]
            g = img[y, x, 1]
            r = img[y, x, 2]
            cv2.putText(img, str(b) + ',' +
                        str(g) + ',' + str(r),
                        (x, y), font, 1,
                        (255, 255, 0), 2)
            cv2.imshow('image', img)

    #finding the file path to open
    filedir = r'\Users\muhdm\PycharmProjects\pythonProject1\image_split'
    data_path = os.path.join(filedir, '*g')

    files = glob.glob(data_path)
    data = []
    i=0

    def click_event_wrapper(event):
        click_event(event, event.x, event.y, None, None)
    #iterate through each image
    for f1 in files:
        img = cv2.imread(f1,1)
        data.append(img)
        width = 1000
        height = 1000
        dim = (width, height)

        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        # displaying the image
        cv2.imshow('image', img)

        # setting mouse handler for the image
        # and calling the click_event() function
        cv2.setMouseCallback('image', click_event)

        # wait for a key to be pressed to exit
        cv2.waitKey(0)



        # close the window
        cv2.destroyAllWindows()
        print(cord)
        filename = 'coordinates' + str(i) +'.txt'
        fh = open(filename, 'w')
        for pairxy in cord:
            fh.write(pairxy +",")
        fh.close()
        cord.clear()
        i = i+1

    cal.calculate()

if __name__ == "__CoordinateClick__":
    CoordinatePicker()