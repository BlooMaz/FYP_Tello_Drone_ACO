import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg





def create_figure(coords):


    # Create a figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1000)  # Set X-axis limits
    ax.set_ylim(0, 1000)  # Set Y-axis limits

    marker_img = mpimg.imread('drone_pointer.png')  # Replace with the path to your image file

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

    plt.pause(5.0)
    plt.close()
    # Show the final plot
    plt.show()
    plt.pause(5.0)
    plt.close()