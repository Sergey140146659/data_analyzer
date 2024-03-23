import numpy as np
from PRAOF.analytical_functions.envelopes import envelopes
from PRAOF.analytical_functions.smoothing_funcs import supsmooth
from PRAOF.graphics.amplitudes import amplitudes
from PRAOF.graphics.approximation import approximation
from PRAOF.graphics.scatter import scatter_plot


points = [13.2, 11.9, 11.9, 13.4, 13.4, 13.3, 11.9, 12.1, 12.6, 13.9,
          10.7, 12.3, 10.6, 10.4, 10.6, 11.0, 11.0, 10.8, 10.8, 10.6,
          10.9, 11.9, 11.6, 11.9, 11.3, 11.9, 11.4, 11.3, 11.0, 10.8,
          10.9, 10.9, 11.0, 11.2, 11.8, 11.8, 12.7, 12.9, 12.4, 14.2,
          14.8, 14.8, 15.4, 14.6, 14.1, 13.3, 12.6, 11.1, 11.2, 11.6]


x = [i for i in range(len(points))]
scatter_plot(x=x, y=points, title="График точек", xlabel='Значения X', ylabel='Значения Y', png_name=None)

k = 2
smoothed_points = supsmooth(points, k)
smoothed_points = supsmooth(smoothed_points, k)
scatter_plot(x=x, y=points, x_1=x, y_1=smoothed_points, title="График точек", xlabel='Значения X', ylabel='Значения Y',
             png_name=None)

f_x = approximation(x=x, y=smoothed_points, degree=11, title='Аппроксимация данных', xlabel='Значения X',
                    ylabel='Значения Y',
                    png_name=None)

greater_zero = []
less_zero = []
for point, approximation_point in zip(points, smoothed_points):
    # point = i
    # approximation_point = f_x(point)
    if point < approximation_point:
        less_zero.append(-abs(point - approximation_point))
    else:
        greater_zero.append(abs(point - approximation_point))
greater_zero = sorted(greater_zero, reverse=True)
less_zero = sorted(less_zero)
amplitudes(less_zero=less_zero, greater_zero=greater_zero, title="Амплитуды значений", xlabel='Индекс',
           ylabel='Разница')

envelopes_info = {}
greater_envelopes = envelopes(x, greater_zero)
envelopes_info['x_data_greater'] = np.array(x)
envelopes_info['popt_greater'] = greater_envelopes['popt']

less_envelopes = envelopes(x, less_zero)
envelopes_info['x_data_less'] = np.array(x)
envelopes_info['popt_less'] = less_envelopes['popt']
amplitudes(less_zero=less_zero, greater_zero=greater_zero, envelopes=envelopes_info, title="Амплитуды значений",
           xlabel='Индекс',
           ylabel='Разница')
