from copy import copy

import matplotlib.pyplot as plt
import numpy as np


def model_func(x, c1, a1, c2, a2):
    return c1 * np.exp(a1 * x) + c2 * np.exp(a2 * x)


def amplitudes(less_zero, greater_zero, envelopes=None, title='title', xlabel='xlabel',
               ylabel='ylabel', png_name=None, **kwargs):
    plt.rc('font', size=30)
    plt.figure(figsize=(20, 15))
    plt.clf()
    greater_zero = sorted(greater_zero, reverse=True)
    less_zero = sorted(less_zero)

    for i in range(len(greater_zero)):
        plt.bar(i, greater_zero[i], width=1.0, color='skyblue')
        plt.plot(i, greater_zero[i], marker='o', markersize=10, color='blue')

    for i in range(len(less_zero)):
        plt.bar(i, less_zero[i], width=1.0, color='salmon')
        plt.plot(i, less_zero[i], marker='o', markersize=10, color='red')
    plt.xlim(0, max(len(less_zero), len(greater_zero)) + 1)
    plt.axhline(0, color='gray', linewidth=0.8, xmin=0, xmax=max(len(less_zero), len(greater_zero)) + 1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # plt.xticks(range(len(greater_zero)))
    if envelopes is not None:
        x_data_greater = envelopes['x_data_greater']
        popt_greater = envelopes['popt_greater']
        plt.plot(x_data_greater, model_func(x_data_greater, *popt_greater), color='red',
                 label=r'$y = {0:.2f} \cdot e^{{ {1:.2f} \cdot x}} + {2:.2f} \cdot e^{{ {3:.2f} \cdot x}}$'.format(
                     *popt_greater))

        x_data_less = envelopes['x_data_less']
        popt_less = envelopes['popt_less']
        if popt_less[2] > 0:
            plt.plot(x_data_less, model_func(x_data_less, *popt_less), color='red',
                     label=r'$y = {0:.2f} \cdot e^{{ {1:.2f} \cdot x}} + {2:.2f} \cdot e^{{ {3:.2f} \cdot x}}$'.format(
                         *popt_less))
        else:
            popt_less_2 = copy(popt_less)
            popt_less[2] *= -1

            plt.plot(x_data_less, model_func(x_data_less, *popt_less_2), color='red',
                     label=r'$y = {0:.2f} \cdot e^{{ {1:.2f} \cdot x}} - {2:.2f} \cdot e^{{ {3:.2f} \cdot x}}$'.format(
                         *popt_less))

        plt.legend()

    if png_name is not None:
        plt.savefig(png_name)
