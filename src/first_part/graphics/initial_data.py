from matplotlib import pyplot as plt


def show_points(data, label='', marker='vr', x_ticks=None, x_label='', y_ticks=None, y_label='', name=None): # график точек
    x_axis = [i for i in range(len(data))]
    y_axis = data[:]
    plt.plot(x_axis, y_axis, marker)
    if y_ticks is not None:
        plt.yticks(y_ticks,y_label)
    if x_ticks is not None:
        plt.xticks(x_ticks,x_label)
    plt.title(label)
    if name is not None:
        plt.savefig(f'{name}.png')
    plt.show()