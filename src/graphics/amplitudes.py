from matplotlib import pyplot as plt


def amplitudes(less_zero, greater_zero, title='title', xlabel='xlabel', ylabel='ylabel', png_name='test', **kwargs):
    greater_zero = sorted(greater_zero, reverse=True)
    less_zero = sorted(less_zero)
    plt.figure(figsize=(10, 8))

    for i in range(len(greater_zero)):
        plt.bar(i, greater_zero[i], width=1.0, color='skyblue')
        plt.plot(i + 0.5, greater_zero[i], marker='o', markersize=5, color='blue')

    for i in range(len(less_zero)):
        plt.bar(i, less_zero[i], width=1.0, color='salmon')
        plt.plot(i + 0.5, less_zero[i], marker='o', markersize=5, color='red')

    plt.axhline(0, color='gray', linewidth=0.8)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(range(len(greater_zero)))
    if png_name is not None:
        plt.savefig(f'{png_name}.png')
    plt.show()
