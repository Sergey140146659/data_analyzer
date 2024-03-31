import json

def round_dict(init_dict):
    answer = []
    for x in init_dict.items():
        if type(x[1]) is int:
            answer.append(x)
        elif type(x[1]) is float:
            answer.append((x[0], round(x[1],2)))
        elif type(x[1]) is str:
            answer.append(x)
        elif type(x[1]) is list:
            add = []
            for y in x[1]:
                if type(y) is int:
                    add.append(y)
                elif type(y) is float:
                    add.append(round(y,2))
                elif type(y) is list:
                    add.append([round(y[0],2),round(y[1],2)])
            answer.append((x[0],add))
    return dict(answer)



def set_initial_state(json_path, init_dict):
    init_dict['data_sorted'] = sorted(init_dict['data'])
    with open(json_path, 'w') as file:
        json.dump(init_dict, file)

def fst_set_values(json_name,k):  # получение первых констант на основе набора данных
    with open(json_name, 'r') as file:
        info = json.load(file)
    info['n'] = len(info['data'])
    info['x_min'] = min(info['data'])
    info['x_max'] = max(info['data'])
    info['R'] = info['x_max'] - info['x_min']
    if k == 0:
        info['k'] = int(info['n'] ** 0.5)
    else:
        info['k'] = k
    info['d'] = info['R'] / info['k']
    with open(json_name, 'w') as file:
        json.dump(info, file)


def get_intervals(json_name): # получение границ интервалов
    with open(json_name, 'r') as file:
        info = json.load(file)
    inters = []
    start_int = info['x_min']
    for _ in range(info['k']):
        end_int = start_int + info['d']
        inters.append((start_int, end_int))
        start_int = end_int
    info['intervals'] = inters
    with open(json_name, 'w') as file:
        json.dump(info, file)


def get_emp_freqs(json_name): # получение эмпирических частот
    with open(json_name, 'r') as file:
        info = json.load(file)
    intervals = info['intervals']
    emp = [0 for _ in range(len(intervals))]
    for ind in range(len(intervals)):
        cnt = 0
        for point in info['data_sorted']:
            if round(intervals[ind][0], 2) <= point < round(intervals[ind][1], 2):
                cnt += 1
        if ind == len(intervals) - 1:
            cnt += 1
        emp[ind] = cnt
    info['empirical_frequencies'] = emp
    with open(json_name, 'w') as file:
        json.dump(info, file)


def get_inter_freqs(json_name): # получение интервальных частот
    with open(json_name, 'r') as file:
        info = json.load(file)
    emp_f = info['empirical_frequencies']
    inter_freqs = []
    for i in range(len(emp_f)):
        inter_freqs.append(emp_f[i]/info['n'])
    info['interval_frequencies'] = inter_freqs
    with open(json_name, 'w') as file:
        json.dump(info, file)


def get_middle_points(json_name): # получение середин интервалов
    with open(json_name, 'r') as file:
        info = json.load(file)
    borders = info['intervals']
    middle_p = []
    for i in range(len(borders)):
        middle_p.append(sum(borders[i])/2)
    info['middle_points'] = middle_p
    with open(json_name, 'w') as file:
        json.dump(info, file)