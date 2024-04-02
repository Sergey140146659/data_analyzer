from fastapi import APIRouter, Response, Request
from first_part.process_data.initial_values import *
from first_part.process_data.empirical_distribution_function import *
from first_part.process_data.empirical_distribution_density import *
from first_part.checking_valid_distr.point_estimation import *
from first_part.checking_valid_distr.check_distribution import *
from first_part.graphics.initial_data_show import *
from first_part.graphics.empirical_distribution_function_show import *
from first_part.graphics.empirical_distribution_density_show import *

obj = {"data":[56.12, 56.75, 53.02, 53.86, 50.45, 50.25, 52.22, 55.38, 51.85, 52.87, 51.41, 45.36, 59.1, 60.05, 58.92, 60.28, 53.42, 60.21, 57.76, 60.11, 59.04, 59.68, 57.48, 57.2, 58.97, 58.24, 55.97, 51.8, 57.74, 57.59, 60.32, 56.28, 59.54, 56.49, 54.58, 59.56, 55.62, 57.7, 56.17, 55.24, 54.0, 55.78, 56.87, 55.62, 72.67, 69.25, 71.41, 69.13, 69.72, 69.24, 67.2, 63.97, 69.27, 68.4, 69.91, 67.5, 67.58, 66.23, 66.19, 65.92, 63.0, 62.0, 62.08, 60.76, 62.03, 60.5, 61.31, 56.72, 65.91, 56.32, 56.23, 57.85, 55.97, 48.6, 56.05, 62.67, 54.55, 61.02, 61.39, 53.66, 61.37, 61.22, 58.48, 61.63, 69.4, 60.03, 63.44, 67.21, 63.43, 63.3, 67.17, 66.23, 66.9, 64.26, 64.38, 69.05, 64.38, 66.44, 44.82, 46.73, 44.21, 43.09, 46.77, 42.07, 42.58, 45.11, 45.25, 45.5, 45.34, 46.39, 43.33, 47.84, 43.53, 44.12, 37.54, 39.16, 43.15, 38.24, 36.22, 36.41, 39.45, 39.91, 39.42, 39.74, 39.96, 38.39, 44.79, 45.44, 54.59, 56.42, 55.15, 52.6, 54.2, 56.11, 48.44, 41.74, 41.88, 44.1, 44.8, 44.73, 68.59, 68.34, 70.62, 69.51, 69.03, 68.18, 63.33, 62.9, 64.04, 65.22, 71.36, 67.15, 65.12, 64.79, 65.05, 65.63, 66.59, 65.09, 63.89, 65.52, 64.26, 60.36, 59.62, 62.5, 62.79, 67.17, 59.6, 63.84, 55.52, 60.76, 67.05, 63.29, 65.33, 60.5, 58.29, 55.76, 53.58, 54.86, 55.61, 64.24, 62.26, 58.18, 54.25, 56.5, 62.21, 62.06, 52.6, 52.67, 49.23, 44.41, 51.34, 59.35, 44.82, 41.38, 56.67, 57.95, 58.68, 56.69, 58.28, 58.01, 58.29, 58.92, 57.44, 57.95, 58.21, 58.05, 52.1, 53.61, 46.51, 46.32, 53.54, 50.88, 52.57, 55.51, 51.22, 51.14, 54.94, 49.75, 54.34, 52.43, 48.95, 50.06, 50.96, 52.72, 54.57, 56.99, 53.9, 54.69, 55.13, 55.99, 55.99, 54.25, 45.45, 43.16, 50.07, 48.78, 57.05, 53.87, 55.02, 54.62, 55.7, 55.15, 56.69, 54.25, 54.02, 53.42, 53.34, 53.27, 58.54, 54.62, 51.33, 45.29, 43.73, 43.99, 46.25, 47.39, 46.32, 41.77, 45.72, 51.14, 50.35, 51.89, 48.85, 53.06, 48.09, 50.82, 56.36, 47.66, 40.26, 43.96, 43.7, 44.74, 42.09, 50.19, 50.1, 51.62, 52.82, 52.54, 55.61, 54.49, 49.79, 57.69, 52.62, 52.74, 51.75, 54.94, 47.47, 52.94, 58.14, 55.36, 57.45, 60.58, 60.66, 61.66, 60.14, 59.69, 60.17, 61.04, 50.97, 55.77, 56.7, 48.06, 51.39, 50.72, 48.41, 48.24, 52.91, 50.6, 46.33, 50.54, 46.04, 49.18, 53.67, 50.97, 54.63, 52.52, 54.66, 52.85, 54.07, 56.73, 49.98, 39.57, 52.88, 45.39, 55.21, 46.32, 48.24, 49.55, 48.53, 49.92, 50.23, 51.03, 48.02, 44.33, 37.27, 38.87, 44.21, 40.59, 43.35, 50.31, 51.82, 47.81, 47.56, 51.69, 46.29, 49.78, 39.18, 31.12, 40.3, 35.91]
,
"k":0
     }

json_path = "first_part/info.json"
set_initial_state(json_path, obj)

fst_set_values(json_path, obj['k'])
show_points(json_path, key='data', label='Исходные данные', name='unsorted_data')
show_points(json_path, key='data_sorted', label='Отсортированные исходные данные', name='sorted_data')
get_intervals(json_path)
get_emp_freqs(json_path)
get_inter_freqs(json_path)
get_middle_points(json_path)
get_acc_freqs(json_path)
get_emp_dens(json_path)
get_border_points(json_path)

emp_dist_func_show(json_path, name='emp_distr_function')
emp_dist_func_dens_show(json_path, name='emp_density_no_curve')

get_sample_mean(json_path)
get_sample_var(json_path)
get_corr_sample_var(json_path)
get_sample_asymm(json_path)
get_sample_excess(json_path)
emp_dist_func_dens_show(json_path, distribution_curve='normal', name='emp_density_normal')
emp_dist_func_dens_show(json_path, distribution_curve='lin', name='emp_density_lin')
emp_dist_func_dens_show(json_path, distribution_curve='exp', name='emp_density_exp')

get_theor_freqs(json_path, distribution='normal')
get_theor_freqs(json_path, distribution='exp')
get_theor_freqs(json_path, distribution='lin')
unite_freqs(json_path)
get_chi_squared(json_path, distr='normal')
get_chi_squared(json_path, distr='exp')
get_chi_squared(json_path, distr='lin')
get_statistics(json_path, distr='normal')
get_statistics(json_path, distr='exp')
get_statistics(json_path, distr='lin')

with open(json_path, 'r') as file:
    info_dict = json.load(file)

rounded_dict = round_dict(info_dict)


t_r = tuple(rounded_dict.items())
t = tuple(info_dict.items())
for i in range(len(t_r)):
    print(f'rounded_dict: {t_r[i][0]} - {t_r[i][1]}')
    print(f'info_dict: {t[i][0]} - {t[i][1]}')
    print()