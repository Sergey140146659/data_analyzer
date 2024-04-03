import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from scipy import interpolate
import math

def interpolate_func(data,step = 0.01):
    step = math.ceil(step * len(data))
    y_exp = []
    x_exp = []
    for i in range(0, len(data), step):
        y_exp.append(data[i])
        x_exp.append(i)

    y_exp.append(data[-1])
    x_exp.append(x_exp[-1] + step)

    func = interpolate.interp1d(x_exp, y_exp, kind='cubic')

    return func

def show_interpolated_func(f2, data, title, xlabel, ylabel,png_name):
    plt.rc('font', size=30)
    plt.figure(figsize=(20, 15))
    plt.clf()

    x_fact = np.linspace(0, len(data), len(data) * 2)
    y_fact = [f2(x_fact[i]) for i in range(len(x_fact))]

    plt.plot(x_fact, y_fact, color='red',linewidth = 4, zorder = 2)
    plt.scatter([i for i in range(len(data))], data, s=100, zorder = 1)


    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if png_name is not None:
        plt.savefig(png_name)