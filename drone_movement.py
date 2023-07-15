from djitellopy import Tello
import math as math
import time

tello = Tello()

tello.connect()
tello.takeoff()
def move_coord(x1,y1,x2,y2,distance):
    if x1==x2 and y1==y2:
        tello.send_rc_control(0, 0, 0, 0)

    elif x1==x2 and y1>y2:
        tello.move_back(distance)

    elif x1==x2 and y1<y2:
        tello.move_foward(distance)

    elif y1==y2 and x1>x2:
        tello.move_left(distance)

    elif y1==y2 and x1<x2:
        tello.move_right(distance)

    elif x1>x2 and y1>y2:
        dx= x2-x1
        dy= y2-y1
        angle = math.degrees(math.atan2(dy, dx))
        angle = 180-angle
        tello.rotate_counter_clockwise(angle)
        time.sleep(1)
        tello.move_forward(distance)

    elif x1>x2 and y1<y2:
        dx= x2-x1
        dy= y2-y1
        angle = math.degrees(math.atan2(dy, dx))
        angle = (-angle)
        tello.rotate_counter_clockwise(angle)
        time.sleep(1)
        tello.move_forward(distance)

    elif x1<x2 and y1>y2:
        dx= x2-x1
        dy= y2-y1
        angle = math.degrees(math.atan2(dy, dx))
        angle = 180+angle
        tello.rotate_clockwise(angle)
        time.sleep(1)
        tello.move_forward(distance)

    elif x1<x2 and y1<y2:
        dx= x2-x1
        dy= y2-y1
        angle = math.degrees(math.atan2(dy, dx))
        angle = angle
        tello.rotate_clockwise(angle)
        time.sleep(1)
        tello.move_forward(distance)

# Define a list of coordinates
coordinates = [
    [20, 70],
    [80, 10],
    [50, 90],
    [30, 40],
    [70, 60]
]

horizontal = 0
vertical = 0

# Iterate over the list of coordinates
for i in range(len(coordinates)):
    x = coordinates[i][0]
    y  = coordinates[i][1]

    if i != len(coordinates)-1:
        p=[x,y]
        q=[coordinates[i+1][0],coordinates[i+1][1]]
        distance1=math.dist(p,q)
        move_coord(x,y,coordinates[i+1][0],coordinates[i+1][1],distance1)
    else:
        time.sleep(2)
        break
    time.sleep(2)  # Adjust the duration as needed for each movement


tello.send_rc_control(0, 0, 0, 0)
time.sleep(2)

tello.land()