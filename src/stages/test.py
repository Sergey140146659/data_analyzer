import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

greater_zero = [4.621726759296017, 3.996896177948887, 3.996896177948887, 3.7826485239752934, 3.3450942027297312,
                3.2338223867655884, 3.0090378043676225, 2.4342565732305985, 2.4342565732305985, 2.317162175103885,
                2.317162175103885, 2.1993771375613953, 1.841994991012271, 1.600516386719999, 1.4788540213445671,
                1.4788540213445671, 1.233764967878754, 1.1103734225577, 0.8619900102342228, 0.6116065621826312,
                0.6116065621826312, 0.6116065621826312, 0.6116065621826312, 0.6116065621826312, 0.6116065621826312,
                0.4857176713866149, 0.4857176713866149, 0.23265723789759996, 0.23265723789759996]

x_data = np.array([i for i in range(len(greater_zero))])
y_data = np.array(greater_zero)


# Функция, которую мы хотим подогнать к данным
def model(x, C1, a1, C2, a2):
    return C1 * np.exp(a1 * x) + C2 * np.exp(a2 * x)


best_arg = {'C1': None, 'C2': None, 'a1': None, 'a2': None}
error = 1e30
t = 2
i1 = -t  # c1

# while i1 <= t:
#     i2 = -t
#     while i2 <= t:
#         i3 = -t
#         while i3 <= t:
#             i4 = -t
#             while i4 <= t:
#                 error_cur = 0
#                 for point_e, point in zip([j for j in range(len(greater_zero))], greater_zero):
#                     iz = model(point_e, i1, i2, i3, i4)
#                     error_cur += abs(point - iz)
#                 if error_cur < error:
#                     error = error_cur
#                     best_arg = {'C1': i1, 'a1': i2, 'C2': i3, 'a2': i4}
#                     print(best_arg)
#                 i4 += 0.1
#             i3 += 0.1
#         i2 += 0.1
#     i1 += 0.1
#
# print(best_arg)

import matplotlib.pyplot as plt

# Задаем значения x и y

# Задаем функцию f(x) (например, f(x) = x^2)

# Создаем значения для функции f(x)
f_x = [model(i, C1=2, a1=-0.1, C2=2, a2=-0.1) for i in x_data]

# Строим график точек x и y
plt.scatter(x_data, y_data, color='red', label='Точки x и y')

# Строим график функции f(x)
plt.plot(x_data, f_x, color='blue', label='f(x) = x^2')

# Добавляем легенду
plt.legend()

# Добавляем названия осей
plt.xlabel('x')
plt.ylabel('y')

# Показываем график
plt.show()
