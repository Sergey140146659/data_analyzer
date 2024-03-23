from fastapi import APIRouter, Response, Request
import os
import json
import numpy as np
from PRAOF.analytical_functions.envelopes import envelopes
from PRAOF.analytical_functions.smoothing_funcs import supsmooth
from PRAOF.graphics.amplitudes import amplitudes
from PRAOF.graphics.approximation import get_best_approximation_degree, approximation
from PRAOF.graphics.scatter import scatter_plot

router = APIRouter(
    prefix="/praof",
    tags=["praof"]
)


@router.post("/praof")
async def data_processing(response: Response, obj: dict):
    try:
        scatter_plot(x=[i for i in range(len(obj["data"]))], y=obj["data"], title="График точек",
                     xlabel='Значения X', ylabel='Значения Y', png_name="./PRAOF/praof_pics/points.png")

        supsmooth_points = supsmooth(supsmooth(obj["data"], 2), 2)
        scatter_plot(x=[i for i in range(len(obj["data"]))], y=obj["data"],
                     x_1=[i for i in range(len(obj["data"]))], y_1=supsmooth_points, title="График точек",
                     xlabel='Значения X',
                     ylabel='Значения Y',
                     png_name=f"./PRAOF/praof_pics/smoothed_points{2}.png")

        best_degree = get_best_approximation_degree(x=[i for i in range(len(obj["data"]))], y=supsmooth_points, k=2)

        greater_zero = []
        less_zero = []
        for point, approximation_point in zip(obj["data"], supsmooth_points):
            if point < approximation_point:
                less_zero.append(-abs(point - approximation_point))
            else:
                greater_zero.append(abs(point - approximation_point))
        greater_zero = sorted(greater_zero, reverse=True)
        less_zero = sorted(less_zero)
        amplitudes(less_zero=less_zero, greater_zero=greater_zero, title="Амплитуды значений", xlabel='Индекс',
                   ylabel='Разница')

        envelopes_info = {}
        greater_envelopes = envelopes(greater_zero)
        envelopes_info['x_data_greater'] = np.array([i for i in range(len(obj["data"]))])
        envelopes_info['popt_greater'] = greater_envelopes['popt']

        less_envelopes = envelopes(less_zero)
        envelopes_info['x_data_less'] = np.array([i for i in range(len(obj["data"]))])
        envelopes_info['popt_less'] = less_envelopes['popt']
        amplitudes(less_zero=less_zero, greater_zero=greater_zero, envelopes=envelopes_info, title="Амплитуды значений",
                   xlabel='Индекс',
                   ylabel='Разница', png_name=f"./PRAOF/praof_pics/amplitudes_k={2}_degree={best_degree}.png")
        info = {
            'points_pic': "/PRAOF/praof_pics/points.png",
            'supsmooth_points_pic': f"/PRAOF/praof_pics/smoothed_points{2}.png",
            'approximations_pic': f"/PRAOF/praof_pics/approximation_k={2}_degree={best_degree}.png",
            'amplitudes': f"/PRAOF/praof_pics/amplitudes_k={2}_degree={best_degree}.png",
        }
        file_path = f"./PRAOF/info_praof_k={2}_degree={best_degree}.json"
        with open(file_path, 'w') as file:
            json.dump(info, file)
        return file_path

    except Exception as e:
        response.status_code = 500
        return {"status": "error", "message": str(e)}
