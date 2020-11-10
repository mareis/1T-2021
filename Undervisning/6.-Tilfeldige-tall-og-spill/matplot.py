import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.exp(x) - x**2 + 2*x - 4


x_verdier = np.linspace(-2, 2, 1000)

plt.plot(x_verdier, f(x_verdier))
plt.show()



