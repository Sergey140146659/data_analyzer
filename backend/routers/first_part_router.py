from fastapi import APIRouter, Response, Request
from first_part.process_data.initial_values import *
from first_part.process_data.empirical_distribution_function import *
from first_part.process_data.empirical_distribution_density import *

router = APIRouter(
    prefix="/first_part",
    tags=["first part"]
)


@router.post("/data_processing")
async def data_processing(response: Response, obj: dict):
    try:
        json_path = "./first_part/info.json"
        set_initial_state(json_path, obj)

        fst_set_values(json_path)
        get_intervals(json_path)
        get_emp_freqs(json_path)
        get_inter_freqs(json_path)
        get_middle_points(json_path)
        get_acc_freqs(json_path)
        get_emp_dens(json_path)
        get_middle_points(json_path)

        with open(json_path, 'r') as file:
            info_dict = json.load(file)

        return info_dict
    
    except Exception as e:
        response.status_code = 500
        return {"status": "error", "message": str(e)}