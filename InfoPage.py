from tkinter import *
from PIL import ImageTk, Image
import page2


def openInfopage():
    def backtohome():
        root.destroy()
        page2.openpage()

    root = Tk()
    root.geometry("1920x1080")
    root.title("Info page")

    bts_back = Image.open("back.png")
    resized_image1_back = bts_back.resize((100, 100), Image.ANTIALIAS)
    new_image1_back = ImageTk.PhotoImage(resized_image1_back)

    image = Image.open("info.png")
    background_image = ImageTk.PhotoImage(image)

    canvas = Canvas(root,
                    width=1920,
                    height=1080)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_image, anchor="nw")
    buttonback = Button(root, image=new_image1_back,
                        height=150,
                        width=300,
                        borderwidth=0,
                        bg="#204050",
                        command=backtohome)

    canvas.create_window(1700, 850, anchor="nw", window=buttonback)

    root.mainloop()


