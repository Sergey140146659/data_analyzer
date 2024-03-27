from fastapi import APIRouter, Response, Request
from first_part.process_data.initial_values import *
from first_part.process_data.empirical_distribution_function import *
from first_part.process_data.empirical_distribution_density import *
from first_part.checking_valid_distr.point_estimation import *
from first_part.checking_valid_distr.check_distribution import *
from first_part.graphics.initial_data_show import *
from first_part.graphics.empirical_distribution_function_show import *
from first_part.graphics.empirical_distribution_density_show import *

obj = {"data":[24.7, 24.8, 24.8, 25.4, 25.7, 25.8, 25.7, 26.1, 26.2, 26.2, 26.3, 26.3, 26.4, 26.4, 26.4, 26.5, 26.5, 26.5,
        26.6, 26.7, 26.7, 26.7, 26.8, 26.8, 26.9, 26.9, 27, 27, 27, 27.1, 27.2, 27.2, 27.2,
        27.3, 27.4, 27.5, 27.5, 27.6, 27.6, 27.6, 27.6, 27.6, 27.7, 27.7, 27.8, 27.9, 28.2, 28.6, 28.7, 28.9],
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