from fastapi import APIRouter, Response, Request
from first_part.process_data.initial_values import *
from first_part.process_data.empirical_distribution_function import *
from first_part.process_data.empirical_distribution_density import *
from first_part.checking_valid_distr.point_estimation import *
from first_part.checking_valid_distr.check_distribution import *
from first_part.graphics.initial_data_show import *
from first_part.graphics.empirical_distribution_function_show import *
from first_part.graphics.empirical_distribution_density_show import *


router = APIRouter(
    prefix="/first_part",
    tags=["first part"]
)


@router.post("/data_processing")
async def data_processing(response: Response, obj: dict):
    try:
        json_path = "./first_part/info.json"

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

        get_theor_freqs(json_path,distribution='normal')
        get_theor_freqs(json_path, distribution='exp')
        get_theor_freqs(json_path, distribution='lin')
        unite_freqs(json_path)
        get_chi_squared(json_path,distr='normal')
        get_chi_squared(json_path, distr='exp')
        get_chi_squared(json_path, distr='lin')
        get_statistics(json_path,distr = 'normal')
        get_statistics(json_path, distr='exp')
        get_statistics(json_path, distr='lin')


        with open(json_path, 'r') as file:
            info_dict = json.load(file)

        rounded_dict = round_dict(info_dict)

        return rounded_dict

    except Exception as e:
        response.status_code = 500
        return {"status": "error", "message": str(e)}