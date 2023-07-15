from djitellopy import Tello
import time

tello = Tello()

tello.connect()
tello.takeoff()

# Define a list of coordinates
coordinates = [(100, 100), (200, 100), (200, 200), (100, 200), (100, 100)]

# Iterate over the list of coordinates
for coord in coordinates:
    x, y = coord
    tello.send_rc_control(x, y, 0, 0)
    time.sleep(2)  # Adjust the duration as needed for each movement

# Stop the drone
tello.send_rc_control(0, 0, 0, 0)
time.sleep(2)

tello.land()