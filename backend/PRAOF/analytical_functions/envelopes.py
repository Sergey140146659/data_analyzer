import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def model_func(x, c1, a1, c2, a2):
    return c1 * np.exp(a1 * x) + c2 * np.exp(a2 * x)


def envelopes(y):
    x_data = np.array([i for i in range(len(y))])
    y_data = np.array(y)
    initial_guess = [1.9, -0.1, 1.9, -0.1]
    # Используйте curve_fit для подгонки модели к данным
    popt, pcov = curve_fit(model_func, x_data, y_data, p0=initial_guess, maxfev=10000)

    plt.scatter(x_data, y_data, label='Исходные данные')
    plt.plot(x_data, model_func(x_data, *popt), label='Подогнанная модель', color='red')
    plt.legend()
    plt.show()
    c1_opt, a1_opt, c2_opt, a2_opt = popt
    return {
        'c1': c1_opt,
        'c2': c2_opt,
        'a1': a1_opt,
        'a2': a2_opt,
        'popt': popt

    }
