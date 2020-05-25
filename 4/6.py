def fact(n):
    p = 1
    for i in range(1, n+1):
        p *= i
        yield p

n = int(input('Input n: '))
for el in fact(n):
    print(el)