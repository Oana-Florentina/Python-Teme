# 1.Find The greatest common divisor of multiple numbers read from the console.
n = int(input("number of numbers: "))
a = int(input())
n = n - 1
while n:
    b = int(input())
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    a = b
    n = n - 1
print(a)
