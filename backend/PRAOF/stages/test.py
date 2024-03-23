import json

with open('info_praof.json') as file:
    info = {
        'points': [],
        'supsmooth_points': [],
        'supsmooth_points_pic': [],  # пути к картинкам
        'approximations_pic': [],  # пути к картинкам
        'amplitudes': "",
    }
    json.dump(info, file)
