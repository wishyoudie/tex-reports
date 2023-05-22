import numpy as np

def find_data_characteristics(data_array):
    print("Выборочное среднее =", np.around(np.mean(data_array), 4))
    print("Выборочная медиана =", np.around(np.median(data_array), 4))
    print("Середина размаха =", np.around((np.max(data_array) + np.min(data_array)) / 2), 4)

    mu2 = np.mean((data_array - np.mean(data_array)) ** 2)  # второй центральный момент (дисперсия)
    mu3 = np.mean((data_array - np.mean(data_array)) ** 3)  # третий центральный момент
    mu4 = np.mean((data_array - np.mean(data_array)) ** 4)  # четвертый центральный момент
    print("Второй центральный момент (дисперсия) =", np.around(mu2, 4))
    print("Третий центральный момент =", np.around(mu3, 4))
    print("Четвертый центральный момент =", np.around(mu4, 4))
    print("Коэффициент асимметрии =", np.around(np.mean(mu3 / mu2 ** (3 / 2)), 4))
    print("Коэффициент эксцесса =", np.around(np.mean(mu4 / mu2 ** 2) - 3, 4))

    IQR = np.percentile(data_array, 75) - np.percentile(data_array, 25)  # интерквартильный размах
    q1 = np.percentile(data_array, 25)  # первый квартиль
    q3 = np.percentile(data_array, 75)  # третий квартиль
    Jp = [q1 - 1.5 * IQR, q3 + 1.5 * IQR]  # интерквантильный промежуток вероятности P = 0.95
    print("Границы интерквантильного промежутка (P = 0.95):", Jp)
    return


def part21(data, random_data):
    print("Основная выборка")
    find_data_characteristics(data)
    print()
    print("Случайная выборка")
    find_data_characteristics(random_data)
    print()
    return