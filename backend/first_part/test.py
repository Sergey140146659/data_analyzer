import json

from backend.first_part.load_data.initial_values import *
from backend.first_part.graphics.initial_data import *

data = [24.7, 24.8, 24.8, 25.4, 25.7, 25.8, 25.7, 26.1, 26.2, 26.2, 26.3, 26.3, 26.4, 26.4,26.4, 26.5, 26.5, 26.5,
        26.6, 26.7, 26.7, 26.7, 26.8, 26.8, 26.9, 26.9, 27,   27,   27,   27.1, 27.2, 27.2, 27.2,
        27.3, 27.4, 27.5, 27.5, 27.6, 27.6, 27.6, 27.6, 27.6, 27.7, 27.7, 27.8, 27.9, 28.2, 28.6, 28.7, 28.9]

with open('info.json','w') as file:
    json.dump({'data':data,'data_sorted': sorted(data),'k':-1},file)

info = fst_set_values('info.json')

show_points(info['data'])
show_points(info['data_sorted'])



