import json
'''
def get_dict(json_name):
    with open('info.json', 'r') as file:
        dictin = json.load(file)
    return dictin

from backend.first_part.process_data.initial_values import *
from backend.first_part.graphics.initial_data_show import *
from backend.first_part.graphics.empirical_distribution_function_show import *
from backend.first_part.process_data.empirical_distribution_function import *
from backend.first_part.process_data.empirical_distribution_density import *
from backend.first_part.graphics.empirical_distribution_density_show import *
from backend.first_part.checking_valid_distr.point_estimation import *
from backend.first_part.checking_valid_distr.uniting_freqs import *
from backend.first_part.checking_valid_distr.check_distribution import *



data = [10.9, 10.9, 11.0, 11.2, 11.8, 11.8, 12.7, 12.9, 12.4, 14.2,
14.8, 14.8, 15.4, 14.6, 14.1, 13.3, 12.6, 11.1, 11.2, 11.6,
11.6, 11.5, 11.2, 12.9, 14.1, 14.0, 12.5, 12.5, 10.8, 10.9,
11.3, 11.4, 11.0, 11.9, 12.4, 12.9, 13.0, 13.5, 14.3, 14.6,
14.8, 14.5, 14.0, 13.2, 12.2, 12.1, 12.2, 11.8, 11.2, 10.9]

data = [24.7, 24.8, 24.8, 25.4, 25.7, 25.8, 25.7, 26.1, 26.2, 26.2, 26.3, 26.3, 26.4, 26.4, 26.4, 26.5, 26.5, 26.5,
        26.6, 26.7, 26.7, 26.7, 26.8, 26.8, 26.9, 26.9, 27, 27, 27, 27.1, 27.2, 27.2, 27.2,
        27.3, 27.4, 27.5, 27.5, 27.6, 27.6, 27.6, 27.6, 27.6, 27.7, 27.7, 27.8, 27.9, 28.2, 28.6, 28.7, 28.9]

with open('info.json', 'w') as file:
    json.dump({'data': data, 'data_sorted': sorted(data), 'k': -1}, file)

info = fst_set_values('info.json')

# show_points(info['data'])
# show_points(info['data_sorted'])

get_intervals('info.json')
get_emp_freqs('info.json')
get_inter_freqs('info.json')
get_middle_points('info.json')

get_acc_freqs('info.json')

with open('info.json', 'r') as file:
    dictin = json.load(file)

emp_dist_func_show('info.json')

get_emp_dens('info.json')
get_border_points('info.json')

emp_dist_func_dens_show('info.json')

get_sample_mean('info.json')
get_sample_var('info.json')
get_corr_sample_var('info.json')
get_sample_asymm('info.json')
get_sample_excess('info.json')

v = get_dict('info.json')
print(v['sample_mean'])
print(v['sample_variance'])
print(v['corrected_sample_variance'])
print(v['mean_square_deviation'])
print(v['sample_asymmetry'])
print(v['sample_excess'])


emp_dist_func_dens_show('info.json', distribution_curve='normal')
emp_dist_func_dens_show('info.json', distribution_curve='exp')
emp_dist_func_dens_show('info.json', distribution_curve='lin')

get_theor_freqs('info.json','normal')
unite_freqs('info.json')
with open('info.json', 'r') as file:
    dictin = json.load(file)

print(dictin['united_frequencies'])
print(dictin['united_theoretical_frequencies'])

print('chi',get_chi_squared('info.json'))
print()
get_theor_freqs('info.json', 'exp')
unite_freqs('info.json')
with open('info.json', 'r') as file:
    dictin = json.load(file)

print(dictin['united_frequencies'])
print(dictin['united_theoretical_frequencies'])

print('chi',get_chi_squared('info.json'))
print()
get_theor_freqs('info.json', 'lin')
unite_freqs('info.json')

print(dictin['united_frequencies'])
print(dictin['united_theoretical_frequencies'])

print('chi',get_chi_squared('info.json'))

get_statistics('info.json')

with open('info.json', 'r') as file:
    dictin = json.load(file)

print(dictin['theoretical_distribution_function'])
print(dictin['kolmogorov_statistics'])'''

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

json_path = "info.json"
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
