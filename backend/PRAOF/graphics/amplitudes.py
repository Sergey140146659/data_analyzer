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
        plt.bar(i, greater_zero[i], width=1.0, color='lightblue')
        plt.plot(i, greater_zero[i], marker='o', markersize=10, color='lightseagreen')

    for i in range(len(less_zero)):
        plt.bar(i, less_zero[i], width=1.0, color='palegreen')
        plt.plot(i, less_zero[i], marker='o', markersize=10, color='springgreen')
    plt.xlim(0, max(len(less_zero), len(greater_zero)) + 1)
    plt.axhline(0, color='gray', linewidth=0.8, xmin=0, xmax=max(len(less_zero), len(greater_zero)) + 1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    # plt.xticks(range(len(greater_zero)))
    if envelopes is not None:
        x_data_greater = envelopes['x_data_greater']
        popt_greater = envelopes['popt_greater']
        popt_greater = [round(i,2) for i in popt_greater]
        plt.plot(x_data_greater, model_func(x_data_greater, *popt_greater), color='crimson', linewidth = 4,
                 #label=r'$y = c1 \cdot e^{a1 \cdot x} + c2 \cdot e^{a2 \cdot x}$')
                 label = f'y = {popt_greater[0]} * e^({popt_greater[1]} * x) + {popt_greater[2]} * e^({popt_greater[3]} * x)')
        x_data_less = envelopes['x_data_less']
        popt_less = envelopes['popt_less']
        popt_less = [round(i,2) for i in popt_less]

        plt.plot(x_data_less, model_func(x_data_less, *popt_less), color='crimson',linewidth = 4,
                 label=f'y = {popt_less[0]} * e^({popt_less[1]} * x) + {popt_less[2]} * e^({popt_less[3]} * x)')

        plt.legend()

    if png_name is not None:
        plt.savefig(png_name)
