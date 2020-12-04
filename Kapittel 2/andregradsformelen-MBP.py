from math import sqrt

a = 1
b = 4
c = 3

D = b**2 - 4*a*c

if D < 0:
    print("Likningen har ....")

elif D == 0:
    x = -b/(2*a)
    print(f"Likningen har ...")

elif D > 0:
    x_1 = (-b - sqrt(D))/(2*a)
    x_2 = (-b + sqrt(D))/(2*a)
    print(f"Likningen har ...")

