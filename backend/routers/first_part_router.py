from fastapi import APIRouter, Response, Request
from first_part.process_data.initial_values import *
from first_part.process_data.empirical_distribution_function import *
from first_part.process_data.empirical_distribution_density import *
from first_part.checking_valid_distr.point_estimation import *
from first_part.checking_valid_distr.check_distribution import *

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
        get_intervals(json_path)
        get_emp_freqs(json_path)
        get_inter_freqs(json_path)
        get_middle_points(json_path)
        get_acc_freqs(json_path)
        get_emp_dens(json_path)

        # получение точечных статистических оценок

        get_sample_mean(json_path)
        get_sample_var(json_path)
        get_corr_sample_var(json_path)
        get_sample_asymm(json_path)
        get_sample_excess(json_path)

        get_theor_freqs(json_path)
        unite_freqs(json_path)
        get_chi_squared(json_path)
        get_statistics(json_path)

        with open(json_path, 'r') as file:
            info_dict = json.load(file)

        return info_dict

    except Exception as e:
        response.status_code = 500
        return {"status": "error", "message": str(e)}