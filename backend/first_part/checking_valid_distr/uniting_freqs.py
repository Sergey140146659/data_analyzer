import json


def unite_freqs(json_name, to_unite=None):

    def check_is_fine(mn_val, freqs):
        for freq in freqs:
            if freq < mn_val:
                return False
        return True

    with open(json_name, 'r') as file:
        info = json.load(file)

    min_freq_value = 0.1 * info['n']
    info['min_frequency_value'] = min_freq_value

    theor_frequencies_n = info['theoretical_frequencies_normal'][:]
    theor_frequencies_e = info['theoretical_frequencies_exp'][:]
    theor_frequencies_l = info['theoretical_frequencies_lin'][:]

    frequencies = info['empirical_frequencies'][:]

    if to_unite is None:
        result_freqs = []
        result_th_freqs_n = []
        result_th_freqs_e = []
        result_th_freqs_l = []

        current_sum = 0
        current_th_sum_n = 0
        current_th_sum_e = 0
        current_th_sum_l = 0

        for ind in range(len(frequencies)):
            if current_sum + frequencies[ind] < min_freq_value:
                current_sum += frequencies[ind]
                current_th_sum_n += theor_frequencies_n[ind]
                current_th_sum_e += theor_frequencies_e[ind]
                current_th_sum_l += theor_frequencies_l[ind]
            else:
                result_freqs.append(current_sum + frequencies[ind])
                result_th_freqs_n.append(current_th_sum_n + theor_frequencies_n[ind])
                result_th_freqs_e.append(current_th_sum_e + theor_frequencies_e[ind])
                result_th_freqs_l.append(current_th_sum_l + theor_frequencies_l[ind])
                current_sum = 0
                current_th_sum_n = 0
                current_th_sum_e = 0
                current_th_sum_l = 0

        if current_sum > 0:
            result_freqs.append(current_sum)
            result_th_freqs_n.append(current_th_sum_n)
            result_th_freqs_e.append(current_th_sum_e)
            result_th_freqs_l.append(current_th_sum_l)

        if frequencies[-1] < min_freq_value:
            frequencies = result_freqs[:-2] + [sum(result_freqs[-2:])]
            theor_frequencies_n = result_th_freqs_n[:-2] + [sum(result_th_freqs_n[-2:])]
            theor_frequencies_l = result_th_freqs_l[:-2] + [sum(result_th_freqs_l[-2:])]
            theor_frequencies_e = result_th_freqs_e[:-2] + [sum(result_th_freqs_e[-2:])]
    '''else:
        result_freqs = [0 for i in range(len(frequencies))]
        result_th_freqs = [0 for i in range(len(theor_frequencies))]
        for i in range(len(frequencies)):
            if i == to_unite[0]:
                result_freqs[i] = sum([frequencies[i] for i in to_unite])
                result_th_freqs[i] = sum([theor_frequencies[i] for i in to_unite])
            elif i in to_unite:
                result_freqs[i] = -1
                result_th_freqs[i] = -1
            else:
                result_freqs[i] = frequencies[i]
                result_th_freqs[i] = theor_frequencies[i]

        frequencies = []
        theor_frequencies = []
        for i in range(len(result_freqs)):
            if result_freqs[i] != -1:
                frequencies.append(result_freqs[i])
            if result_th_freqs[i] != -1:
                theor_frequencies.append(result_th_freqs[i])'''
    info['united_frequencies'] = frequencies[:]
    info['united_theoretical_frequencies_normal'] = theor_frequencies_n[:]
    info['united_theoretical_frequencies_exp'] = theor_frequencies_e[:]
    info['united_theoretical_frequencies_lin'] = theor_frequencies_l[:]
    with open(json_name, 'w') as file:
        json.dump(info, file)