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

    theor_frequencies = info['theoretical_frequencies'][:]
    frequencies = info['empirical_frequencies'][:]

    if to_unite is None:
        result_freqs = []
        result_th_freqs = []
        current_sum = 0
        current_th_sum = 0

        for ind in range(len(frequencies)):
            if current_sum + frequencies[ind] < min_freq_value:
                current_sum += frequencies[ind]
                current_th_sum += theor_frequencies[ind]
            else:
                result_freqs.append(current_sum + frequencies[ind])
                result_th_freqs.append(current_th_sum + theor_frequencies[ind])
                current_sum = 0
                current_th_sum = 0

        if current_sum > 0:
            result_freqs.append(current_sum)
            result_th_freqs.append(current_th_sum)

        frequencies = result_freqs[:]
        theor_frequencies = result_th_freqs[:]
    else:
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
                theor_frequencies.append(result_th_freqs[i])
    info['united_frequencies'] = frequencies[:]
    info['united_theoretical_frequencies'] = theor_frequencies[:]
    with open(json_name, 'w') as file:
        json.dump(info, file)