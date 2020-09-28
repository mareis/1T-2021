import math

sum = 0
for n in range(10**6):
    teller = (-1)**n
    nevner = 2*n + 1
    sum = sum + teller/nevner

print(sum*4)
print(math.pi)
