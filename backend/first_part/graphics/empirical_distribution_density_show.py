import json
from matplotlib import pyplot as plt


def emp_dist_func_dens_show(json_name, label='Эмпирическая плотность распределения и полигон частот', x_ticks=None, x_label=r'$x$',
                       y_ticks=None, y_label=r'$f_{\mathrm{n}}^{\mathrm{*}}(x)$',
                       name=None):  # построение эмпирической плотности распределения

    with open(json_name, 'r') as file:
        info = json.load(file)

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

    plt.ylabel(y_label, fontsize=14)
    plt.xlabel(x_label, fontsize=14)

    plt.title(label)

    if name is not None:
        plt.savefig(f'{name}.png')

    plt.show()
