from djitellopy import Tello
import time

def move_tello(coordinates):
    # Connect to the Tello drone
    tello = Tello()
    tello.connect()

    # Takeoff
    tello.takeoff()
    time.sleep(2)

    # Traverse through the list of coordinates
    for coord in coordinates:
        x, y, z, yaw = coord

        # Move the drone to the specified coordinates
        tello.send_rc_control(int(x), int(y), int(z), int(yaw))
        time.sleep(2)  # Adjust the duration based on your requirements

    # Stop and land the drone
    tello.send_rc_control(0, 0, 0, 0)
    time.sleep(2)
    tello.land()

    # Disconnect from the Tello drone
    tello.disconnect()

# Example list of coordinates: [x, y, z, yaw]
coordinates = [
    [0, 0, 20, 0],   # Move forward at 50 cm altitude
    [20, 0, 20, 0],  # Move right at 50 cm altitude
    [0, 0, 0, 0]     # Hover in place
]

# Call the function to move the Tello drone
move_tello(coordinates)