import matplotlib.pyplot as plt


def scatter_plot(x, y, x_1=None, y_1=None, title='title', xlabel='xlabel', ylabel='ylabel', png_name=None, **kwargs):
    plt.rc('font', size=30)
    plt.figure(figsize=(20, 15))
    #plt.figure(figsize=(8, 6))
    plt.clf()
    plt.scatter(x, y, s=100, **kwargs)
    if x_1 is not None:
        plt.scatter(x_1, y_1, s=100, **kwargs)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if png_name is not None:
        plt.savefig(png_name)
