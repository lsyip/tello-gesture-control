from djitellopy import Tello


class TelloGestureController:
    def __init__(self, tello: Tello):
        self.tello = tello
        self._is_landing = False
        self._is_flying = False


    def gesture_control(self, gesture_buffer):
        gesture_id = gesture_buffer.get_gesture()
        print("GESTURE", gesture_id)

        if not self._is_landing:

            if gesture_id == 0:  # TURN MOTOR ON / FORWARD
                if (not self._is_flying):
                    self.tello.turn_motor_on()
                else:
                    self.tello.move_forward(20)

            elif gesture_id == 1: # TURN MOTOR OFF / BACKWARD
                if (not self._is_flying):
                    self.tello.turn_motor_off()
                else:
                    self.tello.move_backward(20)

            elif gesture_id == 2:  # TAKEOFF
                if (not self._is_flying):
                    self.tello.takeoff()
                    self._is_flying = True

            elif gesture_id == 3:  # LAND
                self._is_landing = True
                self.tello.land()
                self._is_flying = False

            elif gesture_id == 4:  # UP
                if (self._is_flying):
                    self.tello.move_up(20)

            elif gesture_id == 5:  # DOWN
                if (self._is_flying):
                    self.tello.move_down(20)

            elif gesture_id == 6:  # RIGHT
                if (self._is_flying):
                    self.tello.move_left(20)

            elif gesture_id == 7:  # LEFT
                if (self._is_flying):
                    self.tello.move_right(20)

            elif gesture_id == 8:  # CW
                if (self._is_flying):
                    self.tello.rotate_clockwise(360)

            elif gesture_id == 9:  # CCW
                if (self._is_flying):
                    self.tello.rotate_counter_clockwise(360)

                
            elif gesture_id == -1:
                self.forw_back_velocity = self.up_down_velocity = \
                    self.left_right_velocity = self.yaw_velocity = 0


