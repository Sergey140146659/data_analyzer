import json

def get_emp_dens(json_name):
    with open(json_name, 'r') as file:
        info = json.load(file)
    inter_freqs = info['interval_frequencies']
    emp_dens = []

    for i in range(len(inter_freqs)):
        emp_dens.append(inter_freqs[i]/info['d'])
    info['empirical_density'] =  emp_dens

    with open(json_name, 'w') as file:
        json.dump(info, file)

def get_border_points(json_name):
    with open(json_name, 'r') as file:
        info = json.load(file)

    borders = sorted([i for i in set([j for sub in info['intervals'] for j in sub])])

    info['border_points'] = borders
    with open(json_name, 'w') as file:
        json.dump(info, file)
