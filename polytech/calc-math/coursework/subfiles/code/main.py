import numpy as np
from scipy.integrate import quad, odeint, solve_ivp
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

f = lambda z: (z)/(np.sin(z) * (np.cos(z) + 0.7 * np.sin(z)))
g = lambda x: x * np.sinh(10 / x) - 15
p = lambda y: y / ((1 + y ** 2) ** 3)

k1 = 0.5686341 # * 0.99
k2 = 0.1622131 # * 0.99
sol1, err = quad(f, 0, np.pi / 2)
c1 = sol1 * k1

sol2 = root_scalar(g, bracket=[1, 10], method='bisect').root
c2 = sol2 * k2

def model(y, t, c2, c1):
    eqy, z = y
    dydt = [z, c1 * p(eqy) - c2 * z]
    return dydt


print(np.around(c1, decimals=12))
print(np.around(c2, decimals=12))

t = np.linspace(0, 1)
y0 = [0.05, 0.]
y = odeint(model, y0, t, args=(c2, c1))
plt.plot(t, y[:, 0], label=r'$y(t)$')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend(loc='best', fontsize=12)
plt.savefig('../images/graph.png')
plt.show()
