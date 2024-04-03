from fastapi import APIRouter, Response
import json
import numpy as np
from PRAOF.analytical_functions.envelopes import envelopes
from PRAOF.analytical_functions.smoothing_funcs import supsmooth
from PRAOF.graphics.amplitudes import amplitudes
from PRAOF.graphics.approximation import get_best_approximation_degree, approximation
from PRAOF.graphics.scatter import scatter_plot
from PRAOF.graphics.interpolate import *

router = APIRouter(
    prefix="/praof",
    tags=["praof"]
)


@router.post("/data_processing")
async def data_processing(response: Response, obj: dict):
    try:
        scatter_plot(x=[i for i in range(len(obj["data"]))], y=obj["data"], title="График точек",
                     xlabel='Значения X', ylabel='Значения Y', png_name="../frontend/src/praof_pics/points.png")

        supsmooth_points = supsmooth(supsmooth(obj["data"], 2), 2)
        scatter_plot(x=[i for i in range(len(obj["data"]))], y=obj["data"],
                     x_1=[i for i in range(len(obj["data"]))], y_1=supsmooth_points, title="График точек",
                     xlabel='Значения X',
                     ylabel='Значения Y',
                     png_name=f"../frontend/src/praof_pics/smoothed_points.png")

        inter_func = interpolate_func(supsmooth_points)
        show_interpolated_func(inter_func, obj["data"], title="Интерполяция данных",
                               xlabel='Значения X',
                               ylabel='Значения Y',
                               png_name=f"../frontend/src/praof_pics/interpolated_func.png")

        interpolated_points = [inter_func(i) for i in range(len(obj["data"]))]

        greater_zero = []
        less_zero = []
        for point, approximation_point in zip(obj["data"], interpolated_points):
            if point < approximation_point:
                less_zero.append(-abs(point - approximation_point))
            else:
                greater_zero.append(abs(point - approximation_point))
        greater_zero = sorted(greater_zero, reverse=True)
        less_zero = sorted(less_zero)

        amplitudes(less_zero=less_zero, greater_zero=greater_zero, title="Амплитуды значений", xlabel='Индекс',
                   ylabel='Разница', png_name=f"../frontend/src/praof_pics/amplitudes.png")

        envelopes_info = {}

        greater_envelopes = envelopes(greater_zero)
        envelopes_info['x_data_greater'] = np.array([i for i in range(len(obj["data"]))])
        envelopes_info['popt_greater'] = greater_envelopes['popt']

        less_envelopes = envelopes(less_zero)

        envelopes_info['x_data_less'] = np.array([i for i in range(len(obj["data"]))])
        envelopes_info['popt_less'] = less_envelopes['popt']

        amplitudes(less_zero=less_zero, greater_zero=greater_zero, envelopes=envelopes_info, title="Амплитуды значений",
                   xlabel='Индекс',
                   ylabel='Разница', png_name=f"../frontend/src/praof_pics/amplitudes_with_curves.png")

        ret_greater_env = [round(i, 2) for i in greater_envelopes['popt']]
        ret_less_env = [round(i, 2) for i in less_envelopes['popt']]

        info_ret = {'points_pic': "praof_pics/points.png",
                    'supsmooth_points_pic': f"praof_pics/smoothed_points.png",
                    'interpolation_pic': f"praof_pics/interpolated_func.png",
                    'amplitudes': f"praof_pics/amplitudes.png",
                    'amplitudes_with_curves': f"praof_pics/amplitudes_with_curves.png",
                    'coefs_greater': ret_greater_env,
                    'coefs_less': ret_less_env
                    }

        return info_ret



    except Exception as e:
        response.status_code = 500
        return {"status": "error", "message": str(e)}
