from djitellopy import Tello
import time

tello = Tello()

tello.connect()
tello.takeoff()

# Define a list of coordinates
coordinates = [[100, 100], [200, 100], [100, 300], [100, 200], [100, 100]]
horizontal = 0
vertical = 0
# Iterate over the list of coordinates
for i in range(len(coordinates)):
    x = coordinates[i][0]
    y  = coordinates[i][1]

    horizontal = x - horizontal
    vertical = y - vertical
    print(horizontal)
    print(vertical)
    print(" ")
    tello.send_rc_control(x, y, 0, 0)
    time.sleep(2)  # Adjust the duration as needed for each movement


tello.send_rc_control(0, 0, 0, 0)
time.sleep(2)

tello.land()