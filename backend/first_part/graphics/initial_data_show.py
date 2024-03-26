from matplotlib import pyplot as plt
import json

def show_points(json_name, key, label='', marker='vr', x_ticks=None, x_label='', y_ticks=None, y_label='', name=None): # график точек

    with open(json_name, 'r') as file:
        info = json.load(file)

    data = info[key]
    plt.rc('font', size=30)
    plt.figure(figsize=(20, 15))
    plt.clf()

    x_axis = [i for i in range(len( data))]
    y_axis = data[:]
    plt.plot(x_axis, y_axis, marker, markersize = 25)
    if y_ticks is not None:
        plt.yticks(y_ticks,y_label)
    if x_ticks is not None:
        plt.xticks(x_ticks,x_label)
    plt.title(label)
    if name is not None:
        plt.savefig(f'../frontend/src/first_part_pics/{name}.png')
    info[name] = f'first_part_pics/{name}.png'
    with open(json_name, 'w') as file:
        json.dump(info, file)