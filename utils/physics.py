import math
import numpy
import matplotlib.pyplot as plt

force_integral = 0
pi = math.pi
interval = 1

def current(theta, theta_minus, kp, ki, kd):
    k_theta_to_force = 10
    force = k_theta_to_force * math.tan(theta)
    force_minus = k_theta_to_force * math.tan(theta_minus)
    f = -  (kp * proportional(force) + kd * differential(force, force_minus) +
        ki * integral(force, force_minus))
    # print('Force: ' + str(f))
    return f


def proportional(force):
    return force


def differential(force, force_minus):
    global interval
    d = (force - force_minus)/interval
    return d


def integral(force, force_minus):
    global interval
    force_threshold_integral = 20
    if (force > -force_threshold_integral and
         force < force_threshold_integral):
        force_integral = 0
    i = force_integral + interval * (force + force_minus)/2
    return i


def test_sinusoidal_theta():
    global pi
    
    kp = 0
    ki = 0
    kd =10
    
    theta_initial = 0
    theta_minus = theta_initial
    theta =1
    theta_array = []
    current_array = []

    for angle in numpy.arange(-pi/2, pi/2, 0.01):
        theta = math.sin(angle)
        print('Theta: ' + str(theta*180/pi))
        curr = current(theta, theta_minus, kp, ki, kd)
        print('Current: ' + str(curr) + '\n')

        theta_minus = theta
        theta_array.append(theta)
        current_array.append(curr)

    print len(theta_array)
    print len(current_array)
    plt.subplot(211)
    plt.plot(theta_array)
    plt.subplot(212)
    plt.plot( current_array)
    # plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    test_sinusoidal_theta()
