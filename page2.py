from tkinter import *
from PIL import Image, ImageTk
import pageAfter
import InfoPage
import telloc


def openpage():
    def subOpenPage1():
        # go to next page which is choose the file image
        window.destroy()
        pageAfter.startPage()

    def subOpenPage2():
        # go to next page which is choose the file image
        window.destroy()
        InfoPage.openInfopage()

    def subOpenPage3():
        # go to next page which is choose the file image
        window.destroy()
        telloc.main()

    # test image
    fileimg1 = "paddy.jpg"

    window = Tk()
    # size of window
    window.geometry("1920x1080")
    window.title("HomePage")

    bg = PhotoImage(file="homebg.png")

    # login button image
    bts = Image.open("start_button_home.png")
    resized_image1 = bts.resize((300, 150), Image.ANTIALIAS)
    new_image1 = ImageTk.PhotoImage(resized_image1)

    # cotroller button image
    btsc = Image.open("start_button_home.png")
    resized_image1c = btsc.resize((300, 150), Image.ANTIALIAS)
    new_image1c = ImageTk.PhotoImage(resized_image1c)

    # exit button image
    bts_exit = Image.open("logout.png")
    resized_image1_exit = bts_exit.resize((100, 100), Image.ANTIALIAS)
    new_image1_exit = ImageTk.PhotoImage(resized_image1_exit)

    # info button image
    bts_info = Image.open("infoicon2.png")
    resized_image1_info = bts_info.resize((150, 150), Image.ANTIALIAS)
    new_image1_info = ImageTk.PhotoImage(resized_image1_info)

    # Create Canvas
    canvas1 = Canvas(window, width=1920,
                     height=1080)

    canvas1.pack(fill="both", expand=True)

    # Display image
    canvas1.create_image(0, 0, image=bg,
                         anchor="nw")

    # create button
    buttonStart = Button(window, image=new_image1, height=150, width=300, borderwidth=0, bg="#204050",
                         command=subOpenPage1)
    buttonInfo = Button(window, image=new_image1_info, height=150, width=150, borderwidth=0, bg="#204050",
                         command=subOpenPage2)
    buttonc = Button(window, image=new_image1c, height=150, width=150, borderwidth=0, bg="#204050",
                        command=subOpenPage3)

    buttonExit = Button(window, image=new_image1_exit, bg="#FFFFFF", text="Exit", command=window.quit, borderwidth=0)

    # display button
    canvas1.create_window(900, 600, anchor="nw", window=buttonStart)
    canvas1.create_window(700, 600, anchor="nw", window=buttonc)
    canvas1.create_window(500, 600, anchor="nw", window=buttonInfo)
    canvas1.create_window(1750, 900, anchor="nw", window=buttonExit)

    window.mainloop()

if __name__ == "__page2__":
    openpage()