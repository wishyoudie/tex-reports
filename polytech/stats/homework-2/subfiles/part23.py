import numpy as np
from scipy import stats

def find_interval_chars_part(data_array):
    Q = 0.95
    n = len(data_array)
    mean = np.mean(data_array)
    var = np.var(data_array, ddof=1)
    std_error = stats.sem(data_array)
    t_value = stats.t.ppf((1 + Q) / 2, n - 1)

    # интервальные оценки для первого начального момента (среднего)
    ci_mean = (mean - t_value * std_error, mean + t_value * std_error)

    # интервальные оценки для второго центрального момента (несмещенной выборочной дисперсии)
    chi2_value = stats.chi2.interval(Q, df=n - 1)
    ci_var = ((n - 1) * var / chi2_value[1], (n - 1) * var / chi2_value[0])

    print("Первый начальный момент: ", mean)
    print("Интервальные оценки для первого начального момента: ", ci_mean)
    print("Второй центральный момент: ", var)
    print("Интервальные оценки для второго центрального момента: ", ci_var)
    return Q, n, mean, std_error


def find_interval_chars(data_array):
    Q, n, mean, std_error = find_interval_chars_part(data_array)
    t_value = 2.2261
    ci_lower = mean - t_value * std_error
    ci_upper = mean + t_value * std_error
    k = 1
    sorted_data = np.sort(data_array)
    trimmed_data = sorted_data[k:n - k]
    alpha = 1 - Q
    tolerance = np.percentile(trimmed_data, [(1 - alpha) / 2 * 100, (1 + alpha) / 2 * 100])
    lower = tolerance[0]
    upper = tolerance[1]
    print(f"Интерквантильный промежуток (параметрический подход): ({ci_lower:.3f}, {ci_upper:.3f})")
    print(f"Интерквантильный промежуток (непараметрический подход): ({lower:.3f}, {upper:.3f})")
    return


def part23(data, random_data):
    print("Основная выборка")
    find_interval_chars(data)
    print()
    print("Случайная выборка")
    find_interval_chars_part(random_data)
    print()
    return