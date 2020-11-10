import numpy.random as rd
a = rd.randint(-5, 5)
print(f'a = {a}')

b = rd.uniform(0, 10)
print(f'b = {b}')

c = rd.randint(100, 200, 5)
print(f'c = {c}')

d = rd.randint(50, 100, 5)*2
print(f'd = {d}')
