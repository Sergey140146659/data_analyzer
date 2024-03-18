import numpy as np
import matplotlib.pyplot as plt


def approximation(x, y, degree=2, title='title', xlabel='xlabel', ylabel='ylabel', png_name=None, **kwargs):
    # Полиномиальная аппроксимация
    coefficients = np.polyfit(x, y, degree)
    poly = np.poly1d(coefficients)

    # Генерация значений для графика
    x_new = np.linspace(x[0], x[-1], abs(x[-1] - x[0]) * 100)
    y_new = poly(x_new)

    plt.scatter(x, y)
    plt.plot(x_new, y_new, 'r', label=f'Аппроксимация (полином степени {degree})')
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if png_name is not None:
        plt.savefig(f'{png_name}.png')
    plt.show()
    return poly