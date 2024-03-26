import json

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
print(dictin['kolmogorov_statistics'])