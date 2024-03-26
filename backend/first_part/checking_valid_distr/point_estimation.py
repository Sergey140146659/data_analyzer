import json


def get_sample_mean(json_name):  # получение выборочного среднего
    with open(json_name, 'r') as file:
        info = json.load(file)

    a = info['middle_points']
    p = info['interval_frequencies']

    sample_mean = sum([a[i] * p[i] for i in range(len(a))])

    info['sample_mean'] = sample_mean

    with open(json_name, 'w') as file:
        json.dump(info, file)


def get_sample_var(json_name):  # получение выборочной дисперсии
    with open(json_name, 'r') as file:
        info = json.load(file)

    a = info['middle_points']
    p = info['interval_frequencies']
    x = info['sample_mean']

    s = sum([a[i] ** 2 * p[i] for i in range(len(a))]) - x ** 2

    info['sample_variance'] = s

    with open(json_name, 'w') as file:
        json.dump(info, file)


def get_corr_sample_var(json_name):  # получение исправленной выборочной дисперсии и выборочного среднего
    # квадратического отклонения
    with open(json_name, 'r') as file:
        info = json.load(file)

    s = info['sample_variance']
    n = info['n']

    samp = (n / (n - 1)) * s
    samp_2 = samp ** 0.5
    info['corrected_sample_variance'] = samp
    info['mean_square_deviation'] = samp_2

    with open(json_name, 'w') as file:
        json.dump(info, file)


def get_sample_asymm(json_name):  # получение выборочной асимметрии
    with open(json_name, 'r') as file:
        info = json.load(file)

    a = info['middle_points']
    s = info['mean_square_deviation']
    x = info['sample_mean']
    p = info['interval_frequencies']

    s_asymm = (1 / (s ** 3)) * sum([(a[i] - x) ** 3 * p[i] for i in range(len(a))])

    info['sample_asymmetry'] = s_asymm

    with open(json_name, 'w') as file:
        json.dump(info, file)


def get_sample_excess(json_name):  # получение выборочного эксцесса
    with open(json_name, 'r') as file:
        info = json.load(file)

    a = info['middle_points']
    s = info['mean_square_deviation']
    x = info['sample_mean']
    p = info['interval_frequencies']

    s_exc = ((1 / (s ** 4)) * sum([(a[i] - x) ** 4 * p[i] for i in range(len(a))])) - 3

    info['sample_excess'] = s_exc

    with open(json_name, 'w') as file:
        json.dump(info, file)
