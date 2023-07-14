import pygame
from djitellopy import Tello

# Initialize the Tello drone
drone = Tello()

# Connect to the Tello drone
drone.connect()

# Initialize Pygame
pygame.init()

# Set up the Pygame window
window_width, window_height = 400, 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tello Drone Controller")

# Function to send commands to the Tello drone
def send_command(command):
    drone.send_command(command)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # Example commands
            if event.key == pygame.K_UP:
                send_command("up 20")
            elif event.key == pygame.K_DOWN:
                send_command("down 20")
            elif event.key == pygame.K_LEFT:
                send_command("left 20")
            elif event.key == pygame.K_RIGHT:
                send_command("right 20")
            elif event.key == pygame.K_SPACE:
                send_command("takeoff")
            elif event.key == pygame.K_RETURN:
                send_command("land")

    # Clear the window
    window.fill((0, 0, 0))

    # Update the window
    pygame.display.flip()

# Disconnect from the Tello drone
drone.disconnect()

# Quit Pygame
pygame.quit()