# Write your code here :-)
import matplotlib.pyplot as plt
from numpy import linspace


def f(x):
    return 2*x


x = linspace(0, 10, 100)

plt.plot(x, f(x))
