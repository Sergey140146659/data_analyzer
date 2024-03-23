import matplotlib.pyplot as plt


def scatter_plot(x, y, x_1=None, y_1=None, title='title', xlabel='xlabel', ylabel='ylabel', png_name=None, **kwargs):
    plt.scatter(x, y, **kwargs)
    if x_1 is not None:
        plt.scatter(x_1, y_1, **kwargs)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if png_name is not None:
        plt.savefig(f'{png_name}.png')
    plt.show()
