import math
import numpy
import matplotlib.pyplot as plt

force_integral = 0
pi = math.pi

def current(theta, theta_minus, kp, kd, ki):
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
    interval = 1
    d = (force - force_minus)/interval
    return d


def integral(force, force_minus):
    interval = 1
    force_threshold_integral = 20
    if (force > -force_threshold_integral and
         force < force_threshold_integral):
        force_integral = 0
    i = force_integral + interval * (force + force_minus)/2
    return i


def test():
    global pi
    theta_initial = 0
    theta =1
    theta_minus = theta_initial
    theta_array = []
    current_array = []
    i = 0
    for angle in numpy.arange(-pi/2, pi/2, 0.1):
        theta = math.sin(angle)
        print('Theta: ' + str(theta*180/pi))
        curr = current(theta, theta_minus, 1, 1, 1)
        print('Current: ' + str(curr))
        print
        theta_minus = theta
        theta_array.append(theta)
        current_array.append(curr)
        i = i + 1
    print theta_array
    print current_array
    plt.subplot(1)
    plt.plot(theta_array)
    plt.subplot(2)
    plt.plot( current_array)

if __name__ == '__main__':
    test()
