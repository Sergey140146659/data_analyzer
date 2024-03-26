from scipy.integrate import quad
import math
import json
from first_part.checking_valid_distr.uniting_freqs import *


def laplas(x):
    def func(arg):
        return pow(math.e,-(arg**2/2))
    return quad(func,0,x)[0]/(2*math.pi)**0.5


def get_theor_freqs(json_name, distribution='normal'):

    # parameters for distribution: 'normal', 'exp', 'lin'

    with open(json_name, 'r') as file:
        info = json.load(file)

    theor_freqs = []

    a = info['border_points']
    x = info['sample_mean']
    s = info['mean_square_deviation']

    if distribution == 'normal':

        for i in range(1, len(a)):
            theor_freqs.append(laplas((a[i] - x)/s) - laplas((a[i-1]-x)/s))

    elif distribution == 'exp':

        lambd = 1/x
        for i in range(1,len(a)):
            theor_freqs.append(pow(math.e, - lambd * a[i]) - pow(math.e, - lambd * a[i-1]))

    else:
        a0 = a[0]
        ak = a[-1]
        for i in range(1,len(a)):
            theor_freqs.append((a[i] - a[i-1])/(ak - a0))

    info['theoretical_probabilities'] = theor_freqs[:]

    info['theoretical_frequencies'] = [theor_freqs[i] * info['n'] for i in range(len(theor_freqs))]

    with open(json_name, 'w') as file:
        json.dump(info, file)


def get_chi_squared(json_name):
    with open(json_name, 'r') as file:
        info = json.load(file)

    emp = info['united_frequencies']
    theor = info['united_theoretical_frequencies']

    chi = sum([(emp[i] - theor[i])**2/theor[i] for i in range(len(emp))])

    info['chi_squared'] = chi

    return chi

def get_statistics(json_name, distr = 'normal'):
    # parameters: 'normal', 'exp', 'lin'
    with open(json_name, 'r') as file:
        info = json.load(file)
    fn = [0] + info['accumulated_frequencies']
    a = info['border_points']
    x = info['sample_mean']
    s = info['mean_square_deviation']

    if distr == 'normal':
        f0 = [0.5 + laplas((a[i] - x)/s) for i in range(len(a))]
    elif distr == 'exp':
        lambd = 1/x
        f0 = [1 - pow(math.e, - lambd * a[i]) for i in range(len(a))]
    elif distr == 'lin':
        a0 = a[0]
        ak = a[-1]
        f0 = [(a[i] - a0)/(ak - a0) for i in range(len(a))]

    info['theoretical_distribution_function'] = f0

    mx = max([abs(fn[i] - f0[i]) for i in range(len(f0))])

    stat = info['n']**0.5 * mx

    info['kolmogorov_statistics'] = stat

    with open(json_name,'w') as file:
        json.dump(info,file)
