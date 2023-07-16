import tkinter as tk
from PIL import ImageTk,Image
import page2
def openPage(length,time):

        root = tk.Tk()
        root.geometry("1920x1080")
        root.title("Result for two Drones")
        root.config(bg="#204050")

        def tohome():
                root.destroy()
                page2.openpage()

        # Load the image
        image23 = Image.open("result.png")
        background_image1 = ImageTk.PhotoImage(image23)

        # Create a Label widget with the image
        background_label = tk.Label(root, image=background_image1)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        result0 = Image.open("figure_2d/0.png")
        result1 = Image.open("figure_2d/1.png")

        result0_resized = result0.resize((600, 400), Image.ANTIALIAS)
        result1_resized = result1.resize((600, 400), Image.ANTIALIAS)

        result0=ImageTk.PhotoImage(result0_resized)
        result1 = ImageTk.PhotoImage(result1_resized)

        result0_label=tk.Label(root,image=result0).place(x=200,y=200)
        result1_label = tk.Label(root, image=result1).place(x=900, y=200)

        label0_time  = tk.Label(text="Time Taken  :"+ str(round(time[0],4))+" seconds",fg="white",font=("Arial", 24),bg="#204050").place(x=200,y=650)
        label1_time = tk.Label(text="Time Taken  :"+ str(round(time[1],4))+" seconds", fg="white", font=("Arial", 24), bg="#204050").place(x=900, y=650)

        label0_length = tk.Label(text="Best Length :"+ str(round(length[0],2)), fg="white", font=("Arial", 24), bg="#204050").place(x=200, y=700)
        label1_Length = tk.Label(text="Best Length :"+ str(round(length[1],2)), fg="white", font=("Arial", 24), bg="#204050").place(x=900, y=700)

        # Home button image
        bthome = Image.open("homeico.png")
        resized_image_home = bthome.resize((50, 50), Image.ANTIALIAS)
        new_image_home = ImageTk.PhotoImage(resized_image_home)

        button = tk.Button(root, image=new_image_home,command=tohome).place(x=1800,y=900)

        root.mainloop()

if __name__ == "__result2drone__":
    openPage()
