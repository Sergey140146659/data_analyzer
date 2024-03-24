import json
import math
import numpy as np

from matplotlib import pyplot as plt


def emp_dist_func_dens_show(json_name, label='Эмпирическая плотность распределения и полигон частот', x_ticks=None, x_label=r'$x$',
                       y_ticks=None, y_label=r'$f_{\mathrm{n}}^{\mathrm{*}}(x)$', distribution_curve=None,
                       name=None):  # построение эмпирической плотности распределения

# parameters for distribution curve: 'normal', 'exp', 'lin', None (without any curve)

    with open(json_name, 'r') as file:
        info = json.load(file)

    def get_curve():
        x_axis_curve = np.arange(info['middle_points'][0], info['middle_points'][-1], 0.01)
        x_axis = info['middle_points']
        if distribution_curve == 'normal':
            y_axis = [normal_curve_func(json_name,x_axis[i]) for i in range(len(x_axis))]
            y_axis_curve = [normal_curve_func(json_name,x_axis_curve[i]) for i in range(len(x_axis_curve))]
        if distribution_curve == 'exp':
            y_axis = [exp_curve_func(json_name, x_axis[i]) for i in range(len(x_axis))]
            y_axis_curve = [exp_curve_func(json_name, x_axis_curve[i]) for i in range(len(x_axis_curve))]
        if distribution_curve == 'lin':
            y_axis = [lin_curve_func(json_name, x_axis[i]) for i in range(len(x_axis))]
            y_axis_curve = [lin_curve_func(json_name, x_axis_curve[i]) for i in range(len(x_axis_curve))]
        return x_axis,y_axis, x_axis_curve, y_axis_curve

    emp_dens = info['empirical_density']
    border_steps = info['border_points']

    y_vert = [i for i in emp_dens for j in range(2)]
    x_vert = [border_steps[0]] + [border_steps[i] for i in range(1, len(border_steps) - 1) for j in range(2)] + [border_steps[-1]]

    for i in range(len(y_vert)):
        plt.plot([x_vert[i]] * 2, [0, y_vert[i]], color='grey')

    y_hor = emp_dens[:]
    x_hor = x_vert[:]

    for i in range(len(y_hor)):
        plt.plot([x_hor[i * 2], x_hor[i * 2 + 1]], [y_hor[i], y_hor[i]], color='grey')

    x = info['middle_points'][:]
    y = emp_dens[:]
    plt.plot(x, y, color='black')

    if x_ticks is not None:
        plt.xticks([round(i,2) for i in x_ticks])

    if y_ticks is not None:
        plt.yticks([round(i,2) for i in y_ticks])

    if distribution_curve is not None:
        x_ax, y_ax, x_ax_curve, y_ax_curve = get_curve()
        plt.plot(x_ax,y_ax,'.', color = 'lightseagreen', markersize = 8)
        plt.plot(x_ax_curve, y_ax_curve, linestyle='--', color='lightseagreen')

    plt.ylabel(y_label, fontsize=14)
    plt.xlabel(x_label, fontsize=14)

    plt.title(label)





    if name is not None:
        plt.savefig(f'{name}.png')

    plt.show()

def normal_curve_func(json_name, x):
    with open(json_name, 'r') as file:
        info = json.load(file)

    a = info['sample_mean']
    sigma = info['mean_square_deviation']

    return (pow(math.e, - ( (x - a)**2 / (2 * sigma ** 2) ) )) / ((2 * math.pi) ** 0.5 * sigma)


def exp_curve_func(json_name, x):
    with open(json_name, 'r') as file:
        info = json.load(file)
    if x<0:
        return 0

    lambd = 1/info['sample_mean']

    return lambd * pow (math.e, - lambd * x)


def lin_curve_func(json_name, x):
    with open(json_name, 'r') as file:
        info = json.load(file)

    x = info['sample_mean']
    s = info['mean_square_deviation']

    a = x - s * (3 ** 0.5)
    b = x + s * (3 ** 0.5)

    return 1/(b-a)