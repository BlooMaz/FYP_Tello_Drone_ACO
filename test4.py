import matplotlib.pyplot as plt

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk



def create_figure(coords,name):


    # Create a figure and axis

    fig, ax = plt.subplots(figsize=(12, 12))  # Adjust the width and height as desired
    ax.set_xlim(0, 1000)  # Set X-axis limits
    ax.set_ylim(0, 1000)  # Set Y-axis limits
    ax.set_title('Simulated Movement of Drone')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')

    # Create a scatter plot with an initial position
    point = ax.scatter(coords[0][0], coords[0][1], marker='o')
    trail, = ax.plot([], [], color='blue')
    trail_x = [coords[0][0]]
    trail_y = [coords[0][1]]

    # Define the number of steps for interpolation
    num_steps = 50  # Increase this value for smoother movement

    # Traverse through the list of coordinates
    for i in range(1, len(coords)):
        # Get the current and next coordinates
        x_current, y_current = coords[i - 1]
        x_next, y_next = coords[i]

        # Calculate the intermediate positions using linear interpolation
        x_interp = np.linspace(x_current, x_next, num=num_steps)
        y_interp = np.linspace(y_current, y_next, num=num_steps)

        # Update the position of the point for each intermediate position
        for j in range(num_steps):
            x, y = x_interp[j], y_interp[j]
            point.set_offsets((x, y))

            # Add the current position to the trail coordinates
            trail_x.append(x)
            trail_y.append(y)

            # Update the trail line
            trail.set_data(trail_x, trail_y)
            plt.pause(0.01)  # Pause for a short duration to observe the movement
            # Check for button press event

    plt.close()
    directory = "figure_4d/"
    filename = str(name) + ".png"
    filepath = directory + filename

    # Create the directory if it doesn't exist
    import os
    os.makedirs(directory, exist_ok=True)

    # Save the plot to the specified directory
    fig.savefig(filepath)
    # Show the final plot
    return fig

def start_plotting(coordinates,save):
    # Coordinates for plotting

    # Create a Tkinter window
    window = tk.Tk()
    window.title("Matplotlib Plot in Tkinter")
    window.geometry("1920x1080")

    # Load the background image
    imagebg = ImageTk.PhotoImage(Image.open("bgother.png"))


    # Create a Label widget with the image
    bg_label = tk.Label(window,image=imagebg)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a FigureCanvasTkAgg widget and attach the figure to it
    canvas = FigureCanvasTkAgg(create_figure(coordinates,save), master=window)
    canvas.draw()

    # Pack the canvas widget into the window
    canvas.get_tk_widget().pack()
    # exit button image
    bts_exit = Image.open("logout.png")
    resized_image1_exit = bts_exit.resize((50, 50), Image.ANTIALIAS)
    new_image1_exit = ImageTk.PhotoImage(resized_image1_exit)
    buttonExit = tk.Button(window, bg="#FFFFFF", text="Exit", command=window.destroy, borderwidth=0,image=new_image1_exit).place(x=1450, y=10)

    # Run the Tkinter event loop
    window.mainloop()