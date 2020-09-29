import math

sum = 0
for n in range(10**7):
    teller = (-1)**n
    nevner = 2*n + 1
    sum = sum + teller/nevner

print(4*sum)
print(math.pi)
