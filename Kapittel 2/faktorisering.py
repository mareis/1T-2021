# Antall løsninger i en andregradslikning
# Vi bruker diskriminenten, D = b**2 - 4*a*c
# Form på likning: a*x**2 + b*x + c = 0

from math import sqrt   # importer sqrt (kvadratrot) fra math-biblioteket

a = 1
b = 4
c = 4

D = b**2 - 4*a*c # Diskriminanten

# Ingen løsning:
if D < 0:
    print("Utrykket kan ikke faktoriseres.")

# En løsning
elif D == 0:
    x = -b/(2*a)
    print(f"{a}x**2 + {b}x + {c} = {a}(x - {x})**2")

# To løsninger
elif D > 0:
    x_1 = (-b - sqrt(D))/(2*a)
    x_2 = (-b + sqrt(D))/(2*a)
    print(f"{a}(x + {-x_1})(x + {-x_2})")

