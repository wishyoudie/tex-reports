from math import fabs

def zeroin(f, sta, stb, eps):
    a = sta
    b = stb

    while fabs(b - a) > eps:
        fa = f(a)
        fb = f(b)
        c = (a + b) / 2
        fc = f(c)
        if fa * fc > 0:
            a = c
        else:
            b = c
    return c


def simpson(f, sta, stb, n):
    dx = (stb - sta) / n
    xs = [sta + dx * i for i in range(0, n + 1)]
    fs = [f(x) for x in xs]
    acc = fs[0] + fs[n]
    for i in range(1, n):
        acc += (4 if i % 2 else 2) * fs[i]
    acc *= dx / 3
    return acc