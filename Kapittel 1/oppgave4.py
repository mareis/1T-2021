from numpy import linspace

def f(x):
    return x**2 - 2

X = linspace(-2, 2, 400);
Y = f(X)

print(f"Nullpunkt:")
for i in range(0, 399):
    if Y[i]*Y[i + 1] <= 0:
        print(f"x = {X[i]:.2f}")