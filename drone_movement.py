

from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

coordinates = [(100, 100), (200, 100), (200, 200), (100, 200), (100, 100)]

for coord in coordinates:
    x, y = coord
    tello.go_to(x, y)

tello.land()