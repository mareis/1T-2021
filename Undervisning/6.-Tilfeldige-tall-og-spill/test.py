import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)


def f(x):
    return np.exp(x) + x ** 2 - 2 * x


plt.plot(x, f(x))
plt.show()

plt.plot(-x, f(-x))
plt.show()
