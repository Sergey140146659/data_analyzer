from fastapi import APIRouter, Response, Request
from first_part.process_data.initial_values import *
from first_part.process_data.empirical_distribution_function import *
from first_part.process_data.empirical_distribution_density import *
from first_part.checking_valid_distr.point_estimation import *
from first_part.checking_valid_distr.check_distribution import *
from first_part.graphics.initial_data_show import *
from first_part.graphics.empirical_distribution_function_show import *
from first_part.graphics.empirical_distribution_density_show import *

obj = {"data": [13.2, 11.9, 11.9, 13.4, 13.4, 13.3, 11.9, 12.1, 12.6, 13.9,
              10.7, 12.3, 10.6, 10.4, 10.6, 11.0, 11.0, 10.8, 10.8, 10.6,
              10.9, 11.9, 11.6, 11.9, 11.3, 11.9, 11.4, 11.3, 11.0, 10.8,
              10.9, 10.9, 11.0, 11.2, 11.8, 11.8, 12.7, 12.9, 12.4, 14.2,
              14.8, 14.8, 15.4, 14.6, 14.1, 13.3, 12.6, 11.1, 11.2, 11.6],
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

get_theor_freqs(json_path)
unite_freqs(json_path)
get_chi_squared(json_path)
get_statistics(json_path)

with open(json_path, 'r') as file:
    info_dict = json.load(file)
