import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, integrate
from scipy.stats import skew, kurtosis, norm, chisquare, chi2, kstest, expon

def part3(data):    
    mu, sigma = np.mean(data), np.std(data)
    x = np.linspace(np.min(data), np.max(data), 100)
    y = expon.pdf(x, scale=sigma)
    plt.hist(data, bins=10, density=True, alpha=0.6, color='black', edgecolor='black', label=r'Выборка')
    plt.plot(x, y, 'r-', lw=2, label=r'Экспоненциальное распределение')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$\varphi^*(x)$')
    plt.title('Гистограмма и плотность экспоненциального распределения', style='italic')
    plt.legend()
    plt.savefig('./fig/3.png')
    plt.show()

    alpha = 0.05
    Xi = 0
    n = len(data)
    hist_new = plt.hist(data, bins=9)
    def get_p(start, end, l): 
        return integrate.quad(lambda x: l * np.exp(-l * x), start, end)[0]
    for i in range(0, 9):
        nk = hist_new[0][i]
        start = hist_new[1][i]
        end = hist_new[1][i + 1]
        pk = get_p(start, end, 1 / sigma)
        Xi += (nk - n * pk) ** 2 / (n * pk)
    p_value = 1 - chi2.cdf(Xi, 8)
    print("Критерий Хи-квадрат: ", end='')
    print(p_value)
    if p_value > alpha:
        print("подходит.")
    else:
        print("не подходит.")
    
    print("Критерий типа Колмогорова-Смирнова: ", end='')
    mu, sigma = expon.fit(data)  # оценка параметров нормального распределения по выборке
    n = len(data)
    kstest_result = kstest(data, 'expon', args=(mu, sigma)) # статистика Колмогорова-Смирнова и p-значение
    D = kstest_result.statistic
    D_alpha = np.sqrt(-np.log(alpha / 2) / (2 * n)) - 1 / (6 * n) # критическое значение статистики Колмогорова-Смирнова
    if D <= D_alpha:
        print("подходит.")
    else:
        print("не подходит.")
    print("Критерий “омега-квадрат” Мизеса: ", end='')
    mu, std = expon.fit(data) # оцениваем параметры экспоненциального распределения по выборке
    data_sorted = np.sort(data)
    # значение эмпирической функции распределения (ECDF)
    ecdf = np.arange(1, len(data_sorted) + 1) / len(data_sorted)
    # значение теоретической функции распределения для экспоненциального распределения с оцененными параметрами
    cdf = expon.cdf(data_sorted, loc=mu, scale=std)
    omega_squared = np.sum((ecdf - cdf) ** 2) # значение статистики критерия Мизеса
    critical_value = 0.461 # критическое значение статистики Мизеса для уровня значимости 0.05 и n=9
    print(omega_squared)
    if omega_squared < critical_value:
        print("подходит.")
    else:
        print("не подходит.")
