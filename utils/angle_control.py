import gyro
import PID_controller
import time

def run_control():
    global Ts
    sampling_interval = 0.1
    gyro.set_Ts(sampling_interval)
    PID_controller.set_Ts(sampling_interval)
    gyro.prepare_sensor()

    while True:
        angle_type = 'roll'
        theta = gyro.read_angle(angle_type)
        time.sleep(gyro.get_Ts())
        # print('Angle(' + angle_type +'): ' + str(angle))
        print('Angle(' + angle_type +'): ' + 'a'*int(70+(100/360)*(theta)))
        # print('Angle(' + angle_type +'): ' + str(theta))
        alpha = -0.5
        kp = 0
        ki = 1
        kd = 0
        C_n =  PID_controller.filter_PID(theta, alpha, kp, ki, kd)
        print('Control: ' + str(C_n))
        print('Control: ' + 'c'*int(70+(100/360)*(C_n)))


if __name__ == '__main__':
    run_control()
