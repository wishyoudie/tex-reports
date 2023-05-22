import numpy as np
import matplotlib.pyplot as plt

def ecdf(data_array):
    n = len(data_array)
    x_sorted = np.sort(data_array)
    f = np.arange(1, n + 1) / n
    return x_sorted, f

def part1(data):
    x, y = ecdf(data)
    plt.step(x, y)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$F^*(x)$')
    plt.title('Выборочная функция распределения', style='italic')
    plt.savefig('./fig/1.png')
    plt.show()
    plt.hist(data, bins=10, density=True, alpha=0.6, color='black', edgecolor='black')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\varphi^*(x)$')
    plt.title('Гистограмма', style='italic')
    plt.savefig('./fig/2.png')
    plt.show()
