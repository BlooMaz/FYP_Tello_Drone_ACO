import cv2
from djitellopy import Tello

# Initialize the Tello drone
drone = Tello()

# Connect to the Tello drone
drone.connect()

# Set up video capture
cap = cv2.VideoCapture(0)

# Create a window to display the drone's video stream
cv2.namedWindow("Tello Stream")

# Function to send commands to the Tello drone
def send_command(command):
    drone.send_command(command)

# Main loop
while True:
    # Read the video stream from the drone
    ret, frame = cap.read()

    # Display the video stream
    cv2.imshow("Tello Stream", frame)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # Exit the loop and close the window if the 'q' key is pressed
    if key == ord('q'):
        break

    # Example commands
    if key == ord('t'):
        drone.takeoff()
    elif key == ord('l'):
        drone.land()t
    elif key == ord('w'):
        send_command("forward 10")
    elif key == ord('s'):
        send_command("back 10")
    elif key == ord('a'):
        send_command("left 10")
    elif key == ord('d'):
        send_command("right 10")

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()