import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def approximation(x, y, degree=2, title='title', xlabel='xlabel', ylabel='ylabel', png_name=None, **kwargs):
    if degree == 0:
        return "The approximation"
    plt.clf()
    # Полиномиальная аппроксимация
    coefficients = np.polyfit(x, y, degree)
    poly = np.poly1d(coefficients)

    # Генерация значений для графика
    x_new = np.linspace(x[0], x[-1], abs(x[-1] - x[0]) * 100)
    y_new = poly(x_new)
    mse = mean_squared_error(y, poly(x))

    plt.scatter(x, y)
    plt.plot(x_new, y_new, 'r', label=f'Аппроксимация (полином степени {degree})')
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if png_name is not None:
        plt.savefig(png_name)
    return poly, mse


def get_best_approximation_degree(x, y, k):
    best_degree = -1
    min_error = 1e18
    for degree in range(1, 20):
        error = approximation(x, y, degree=degree, title='Аппроксимация данных', xlabel='Значения X',
                              ylabel='Значения Y',
                              png_name=f"PRAOF/praof_pics/approximation_k={k}_degree={degree}.png")[1]
        # print(error, degree)
        if error < min_error and abs(error - min_error) > 0.001:
            min_error = error
            best_degree = degree
    return best_degree
