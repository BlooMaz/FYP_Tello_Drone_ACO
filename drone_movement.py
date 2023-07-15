from djitellopy import Tello
import time

tello = Tello()

tello.connect()
tello.takeoff()

# Define a list of coordinates
coordinates = [[30,30], [60, 30], [30, 90], [30, 60], [30, 30]]
horizontal = 0
vertical = 0
# Iterate over the list of coordinates
for i in range(len(coordinates)):
    x = coordinates[i][0]
    y  = coordinates[i][1]
    if i!=0:
       horizontal = x-coordinates[i-1][0]
       vertical = y -coordinates[i-1][1]
    else:
        horizontal = x
        vertical = y
    print(horizontal)
    print(vertical)
    print(" ")
    tello.send_rc_control(horizontal, vertical, 0, 0)
    time.sleep(2)  # Adjust the duration as needed for each movement


tello.send_rc_control(0, 0, 0, 0)
time.sleep(2)

tello.land()