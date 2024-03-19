import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Заданные данные
y = [4.621726759296017, 3.996896177948887, 3.996896177948887, 3.7826485239752934, 3.3450942027297312,
     3.2338223867655884, 3.0090378043676225, 2.4342565732305985, 2.4342565732305985, 2.317162175103885,
     2.317162175103885, 2.1993771375613953, 1.841994991012271, 1.600516386719999, 1.4788540213445671,
     1.4788540213445671, 1.233764967878754, 1.1103734225577, 0.8619900102342228, 0.6116065621826312,
     0.6116065621826312, 0.6116065621826312, 0.6116065621826312, 0.6116065621826312, 0.6116065621826312,
     0.4857176713866149, 0.4857176713866149, 0.23265723789759996, 0.23265723789759996]

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


# Определите модельную функцию
def model_func(x, c1, a1, c2, a2):
    return c1 * np.exp(a1 * x) + c2 * np.exp(a2 * x)


# Ваши данные (замените на свои)
x_data = np.array([i for i in range(len(y))])
y_data = np.array(y)
initial_guess = [1.9, -0.1, 1.9, -0.1]

# Используйте curve_fit для подгонки модели к данным
popt, pcov = curve_fit(model_func, x_data, y_data, p0=initial_guess, maxfev=10000)

c1_opt, a1_opt, c2_opt, a2_opt = popt
print(f"Оптимальные значения параметров: c1 = {c1_opt}, a1 = {a1_opt}, c2 = {c2_opt}, a2 = {a2_opt}")

# Визуализация данных и подогнанной кривой
plt.scatter(x_data, y_data, label='Исходные данные')
plt.plot(x_data, model_func(x_data, *popt), label='Подогнанная модель', color='red')
plt.legend()
plt.show()
