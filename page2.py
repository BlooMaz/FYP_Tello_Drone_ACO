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

        window.destroy()
        root1 =Tk()
        root1.geometry("1920x1080")
        root1.title("Tutorial")
        page = PhotoImage(file="tutorial_page.png")

        def start_telloc():
            root1.destroy()
            telloc.main()

        def backtohome():
            root1.destroy()
            openpage()

        canvas2 = Canvas(root1,width=1920,
                     height=1080)

        canvas2.pack(fill="both", expand=True)

        # Display image
        canvas2.create_image(0, 0, image=page,
                             anchor="nw")

        bts_back = Image.open("back.png")
        resized_image1_back = bts_back.resize((300, 150), Image.ANTIALIAS)
        new_image1_back = ImageTk.PhotoImage(resized_image1_back)

        buttonback = Button(root1, image=new_image1_back,
                            height=150,
                            width=300,
                            borderwidth=0,
                            bg="#204050",
                            command=backtohome)

        canvas2.create_window(1600, 850, anchor="nw", window=buttonback)

        btplay = Image.open("start_icon_button.png")
        resized_image_play = btplay.resize((300, 150), Image.ANTIALIAS)
        new_image_play = ImageTk.PhotoImage(resized_image_play)

        buttonPlay = Button(root1, image=new_image_play, height=150, width=300, borderwidth=0, bg="#204050",command=start_telloc)
        canvas2.create_window(1600, 700, anchor="nw", window=buttonPlay)
        root1.mainloop()




    # test image
    fileimg1 = "paddy.jpg"

    window = Tk()
    # size of window
    window.geometry("1920x1080")
    window.title("HomePage")

    bg = PhotoImage(file="homebg.png")

    # login button image
    bts = Image.open("start_icon_button.png")
    resized_image1 = bts.resize((300, 150), Image.ANTIALIAS)
    new_image1 = ImageTk.PhotoImage(resized_image1)

    # cotroller button image
    btsc = Image.open("control_icon_button.png")
    resized_image1c = btsc.resize((300, 150), Image.ANTIALIAS)
    new_image1c = ImageTk.PhotoImage(resized_image1c)

    # exit button image
    bts_exit = Image.open("logout.png")
    resized_image1_exit = bts_exit.resize((100,100), Image.ANTIALIAS)
    new_image1_exit = ImageTk.PhotoImage(resized_image1_exit)

    # info button image
    bts_info = Image.open("info_icon_button.png")
    resized_image1_info = bts_info.resize((300, 150), Image.ANTIALIAS)
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
    buttonInfo = Button(window, image=new_image1_info, height=150, width=300, borderwidth=0, bg="#204050",
                         command=subOpenPage2)
    buttonc = Button(window, image=new_image1c, height=150, width=300, borderwidth=0, bg="#204050",
                        command=subOpenPage3)

    buttonExit = Button(window, image=new_image1_exit, bg="#FFFFFF", text="Exit", command=window.destroy, borderwidth=0)

    # display button
    canvas1.create_window(230, 450, anchor="nw", window=buttonStart)
    canvas1.create_window(230, 620, anchor="nw", window=buttonc)
    canvas1.create_window(230, 790, anchor="nw", window=buttonInfo)
    canvas1.create_window(1800, 880, anchor="nw", window=buttonExit)

    window.mainloop()

if __name__ == "__page2__":
    openpage()