# 1 1 2 3 5 8 13 21 34 55 89
a = 1
b = 1
print(a)
print(b)

sum = 2

for i in range(3, 101):
    c = a + b
    sum = sum + c
    print(c)
    a = b
    b = c

print(sum)