import json


def get_acc_freqs(json_name):
    with open(json_name, 'r') as file:
        info = json.load(file)
    acc_freqs = []
    for i in range(1,len(info['interval_frequencies']) + 1):
        acc_freqs.append(sum(info['interval_frequencies'][:i]))
    info['accumulated_frequencies'] = acc_freqs
    with open(json_name, 'w') as file:
        json.dump(info, file)
