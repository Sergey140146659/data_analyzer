import json

from matplotlib import pyplot as plt


def emp_dist_func_show(json_name, label='Эмпирическая функция распределения', x_ticks=None, x_label=r'$x$',
                       y_ticks=None, y_label=r'$F_{\mathrm{n}}^{\mathrm{*}}(x)$',
                       name=None):  # построение эмпирической функции распределения

    with open(json_name, 'r') as file:
        info = json.load(file)


    plt.rc('font', size=30)
    plt.figure(figsize=(20, 15))
    plt.clf()

    middle_values = info['middle_points']
    acc_freqs = info['accumulated_frequencies']

    x_axis = middle_values + [middle_values[-1] + info['d']]
    y_axis = acc_freqs + [acc_freqs[-1]]

    for i in range(len(x_axis)):
        plt.plot([x_axis[i]] * 2, [0, y_axis[i]], linestyle='--', color='grey')
    for i in range(len(acc_freqs)):
        plt.plot([x_axis[i], x_axis[i + 1]], [y_axis[i]] * 2, marker='<', markevery=[0], color='black')

    plt.title(label)
    plt.ylabel(y_label, fontsize=30)
    plt.xlabel(x_label, fontsize=30)

    if x_ticks is not None:
        plt.xticks([round(i, 2) for i in x_ticks])
    else:
        plt.xticks(x_axis)
    if y_ticks is not None:
        plt.yticks([round(i, 2) for i in y_ticks])
    else:
        plt.yticks(y_axis)

    if name is not None:
        plt.savefig(f'{name}.png')

    plt.show()
