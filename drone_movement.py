from djitellopy import Tello
import math as math
import time

tello = Tello()

tello.connect()
tello.takeoff()
tello.set_speed(40)
def move_coord(x1,y1,x2,y2,distance):
    if x1==x2 and y1==y2:
        tello.send_rc_control(0, 0, 0, 0)

    elif x1==x2 and y1>y2:
        tello.move_back(int(distance))

    elif x1==x2 and y1<y2:

        tello.move_forward(int(distance))

    elif y1==y2 and x1>x2:
        tello.move_left(int(distance))

    elif y1==y2 and x1<x2:
        tello.move_right(int(distance))

    elif x1>x2 and y1>y2:
        dx= x2-x1
        dy= y2-y1
        angle = math.degrees(math.atan2(dy, dx))
        angle = 180-angle
        tello.rotate_counter_clockwise(int(angle))
        time.sleep(1)
        tello.move_forward(int(distance))
        tello.rotate_clockwise(int(angle))

    elif x1>x2 and y1<y2:
        dx= x2-x1
        dy= y2-y1
        angle = math.degrees(math.atan2(dy, dx))
        angle = (-angle)
        tello.rotate_counter_clockwise(int(angle))
        time.sleep(1)
        tello.move_forward(int(distance))
        tello.rotate_clockwise(int(angle))

    elif x1<x2 and y1>y2:
        dx= x2-x1
        dy= y2-y1
        angle = math.degrees(math.atan2(dy, dx))
        angle = 180+angle
        tello.rotate_clockwise(int(angle))
        time.sleep(1)
        tello.move_forward(int(distance))
        tello.rotate_counter_clockwise(int(angle))

    elif x1<x2 and y1<y2:
        dx= x2-x1
        dy= y2-y1
        angle = math.degrees(math.atan2(dy, dx))
        angle = angle
        tello.rotate_clockwise(int(angle))
        time.sleep(1)
        tello.move_forward(int(distance))
        tello.rotate_counter_clockwise(int(angle))

# Define a list of coordinates
coordinates = [
    [0,0],
    [100,100],
    [200,100],
    [200,200],
    [100,200],

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
    time.sleep(1)  # Adjust the duration as needed for each movement


tello.send_rc_control(0, 0, 0, 0)
time.sleep(2)

tello.land()