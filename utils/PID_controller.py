from collections import deque
import sys
import math
import numpy
import matplotlib.pyplot as plt
pi = math.pi
x = deque([0, 0, 0])
y = deque([0 ,0, 0])
Ts = None


def set_Ts(t):
    global Ts
    Ts = t


def y_n_PID(alpha, kp, ki, kd, x_n, x_n_1, x_n_2, y_n_1, y_n_2):
    global Ts
    a0 = (4*kd + 2*Ts*kp + Ts*Ts*ki)/(Ts*Ts)
    a1 = (2*Ts*Ts*ki - 8*kd)/(Ts*Ts)
    a2 = (4*kd - 2*Ts*kp  + Ts*Ts*ki)/(Ts*Ts)
    y_n = (a0*x_n + a1*x_n_1 +a2*x_n_2 +alpha* y_n_2)
    return y_n


def filter_PID(x_n, alpha, kp, ki, kd):
    global x, y, Ts
    print x
    print y
    print (Ts, kp, ki, kd,  x[0], x[1], x[2], y[1], y[2])

    x0 = x[0]
    x1 = x[1]
    x2 = x[2]
    y1 = y[1]
    y2 = y[2]

    temp = y_n_PID(alpha, kp, ki, kd, x0, x1, x2, y1, y2)

    x.pop()
    y.pop()
    x.appendleft(x_n)
    y.appendleft(temp)
    return y[0]


def limit(x, lim):
    if x > 0:
        return min(x, lim)
    else:
        return max(x, -lim)


def limited_tan(theta, tan_limit):
    temp = limit(math.tan(theta), tan_limit)
    return temp


def main():
    global pi, Ts
    
    theta_err_array = []
    y_array = []

    set_Ts(0.01)
    t_min = 0
    t_max = 1
    f = 5 # frequency of theta_err in Hertz
    alpha = -0
    kp = 0
    ki = 0
    kd = 1
    beta_1 = 1
    beta_2 = 1
    tan_limit = 10

    for time in numpy.arange(t_min, t_max, Ts):
        theta_err = (pi/2)*math.sin(2*pi*f*time)
        y_n =  limit((beta_1 * filter_PID(theta_err, alpha, kp, ki, kd) +
            beta_2 * limited_tan(theta_err, tan_limit)), 6000)
        print y
        theta_err_minus = theta_err
        theta_err_array.append(theta_err)
        y_array.append(y_n)

    print len(theta_err_array)
    print len(y_array)
    print (theta_err_array)
    print (y_array)
    plt.subplot(211)
    plt.plot(theta_err_array)
    plt.subplot(212)
    plt.plot( y_array)
    # plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    main()
