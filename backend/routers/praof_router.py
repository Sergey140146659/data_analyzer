from fastapi import APIRouter, Response, Request
import os
import json

from PRAOF.analytical_functions.smoothing_funcs import supsmooth
from PRAOF.graphics.approximation import get_best_approximation_degree
from PRAOF.graphics.scatter import scatter_plot

router = APIRouter(
    prefix="/praof",
    tags=["praof"]
)


@router.post("/praof")
async def praof(response: Response, obj: dict):
    try:
        scatter_plot(x=[i for i in range(len(obj["data"]))], y=obj["data"], title="График точек",
                     xlabel='Значения X', ylabel='Значения Y', png_name="PRAOF/praof_pics/points.png")

        supsmooth_points_range = [supsmooth(supsmooth(obj["data"], k), k) for k in range(0, 20)]
        for k in range(0, 20):
            scatter_plot(x=[i for i in range(len(obj["data"]))], y=obj["data"],
                         x_1=[i for i in range(len(obj["data"]))], y_1=supsmooth_points_range[k], title="График точек",
                         xlabel='Значения X',
                         ylabel='Значения Y',
                         png_name=f"PRAOF/praof_pics/smoothed_points{k}.png")

        best_degree = get_best_approximation_degree(x=[i for i in range(len(obj["data"]))], y=obj["data"])

        file_path = "PRAOF/info_praof.json"
        with open(file_path) as file:
            info = {
                'points': obj["data"],
                'points_pic': "PRAOF/praof_pics/points",
                'supsmooth_points': supsmooth_points_range,
                'supsmooth_points_pic': [f"PRAOF/praof_pics/smoothed_points{k}.png" for k in range(0, 20)],
                'approximations_pic': [f"PRAOF/praof_pics/approximation_{degree}." for degree in range(0, 20)],
                'best_degree': best_degree,
                'best_k': 2,
                'amplitudes': "",
            }
            json.dump(info, file)

    except Exception as e:
        response.status_code = 500
        return {"status": "error", "message": str(e)}
