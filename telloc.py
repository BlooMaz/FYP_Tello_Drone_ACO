from djitellopy import Tello
import cv2
import pygame
import numpy as np
import time
import page2
# Speed of the drone

S = 60
# Frames per second of the pygame window display
# A low number also results in input lag, as input information is processed once per frame.


FPS = 120


class FrontEnd(object):
    """ Maintains the Tello display and moves it through the keyboard keys.
        Press escape key to quit.
        The controls are:
            - T: Takeoff
            - L: Land
            - Arrow keys: Forward, backward, left and right.
            - A and D: Counter clockwise and clockwise rotations (yaw)
            - W and S: Up and down.


    """

    def __init__(self):
        # Init pygame

        pygame.init()
        w_height = 1000
        w_width = 1800
        # Create pygame window

        pygame.display.set_caption("Tello video stream")
        self.screen = pygame.display.set_mode([w_width ,w_height ])


        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((255, 255, 255))


        # Init Tello object that interacts with the Tello drone
        # 初始化与Tello交互的Tello对象
        self.tello = Tello()

        # Drone velocities between -100~100
        # 无人机各方向速度在-100~100之间
        self.for_back_velocity = 0
        self.left_right_velocity = 0
        self.up_down_velocity = 0
        self.yaw_velocity = 0
        self.speed = 10

        self.send_rc_control = False

        # create update timer
        # 创建上传定时器
        pygame.time.set_timer(pygame.USEREVENT + 1, 1000 // FPS)

    def run(self):

        self.tello.connect()
        self.tello.set_speed(self.speed)

        # In case streaming is on. This happens when we quit this program without the escape key.
        self.tello.streamoff()
        self.tello.streamon()

        frame_read = self.tello.get_frame_read()

        should_stop = False
        while not should_stop:

            for event in pygame.event.get():
                if event.type == pygame.USEREVENT + 1:
                    self.update()
                elif event.type == pygame.QUIT:
                    page2.openpage()
                    should_stop = True
                    self.tello.end()
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        page2.openpage()
                        should_stop = True
                        self.tello.end()
                        pygame.quit()

                    else:
                        self.keydown(event.key)
                elif event.type == pygame.KEYUP:
                    self.keyup(event.key)

            if frame_read.stopped:
                break



            frame = frame_read.frame
            # battery
            text = "Battery: {}%".format(self.tello.get_battery())
            cv2.putText(frame, text, (5, 700 - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            frame = cv2.resize(frame, (1800, 1000))
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            frame = np.flipud(frame)

            frame = pygame.surfarray.make_surface(frame)
            frame_rect = frame.get_rect(center=self.screen.get_rect().center)
            self.screen.blit(frame, frame_rect)
            pygame.display.update()

            time.sleep(1 / FPS)

        # Call it always before finishing. To deallocate resources.

        self.tello.end()

    def keydown(self, key):
        """ Update velocities based on key pressed
        Arguments:
            key: pygame key
        """
        if key == pygame.K_UP:  # set forward velocity
            self.for_back_velocity = S
        elif key == pygame.K_DOWN:  # set backward velocity
            self.for_back_velocity = -S
        elif key == pygame.K_LEFT:  # set left velocity
            self.left_right_velocity = -S
        elif key == pygame.K_RIGHT:  # set right velocity
            self.left_right_velocity = S
        elif key == pygame.K_w:  # set up velocity
            self.up_down_velocity = S
        elif key == pygame.K_s:  # set down velocity
            self.up_down_velocity = -S
        elif key == pygame.K_a:  # set yaw counter clockwise velocity
            self.yaw_velocity = -S
        elif key == pygame.K_d:  # set yaw clockwise velocity
            self.yaw_velocity = S

    def keyup(self, key):
        """ Update velocities based on key released
        Arguments:
            key: pygame key

        """
        if key == pygame.K_UP or key == pygame.K_DOWN:  # set zero forward/backward velocity
            self.for_back_velocity = 0
        elif key == pygame.K_LEFT or key == pygame.K_RIGHT:  # set zero left/right velocity
            self.left_right_velocity = 0
        elif key == pygame.K_w or key == pygame.K_s:  # set zero up/down velocity
            self.up_down_velocity = 0
        elif key == pygame.K_a or key == pygame.K_d:  # set zero yaw velocity
            self.yaw_velocity = 0
        elif key == pygame.K_t:  # takeoff
            self.tello.takeoff()
            self.send_rc_control = True
        elif key == pygame.K_l:  # land
            not self.tello.land()
            self.send_rc_control = False

    def update(self):
        """ Update routine. Send velocities to Tello.

        """
        if self.send_rc_control:
            self.tello.send_rc_control(self.left_right_velocity, self.for_back_velocity,
                self.up_down_velocity, self.yaw_velocity)




def main():
    frontend = FrontEnd()

    # run frontend

    frontend.run()


if __name__ == '__telloc__':
    main()