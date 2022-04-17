from math import factorial


def f(n):
    d = 1
    for i in range(1, n+1):
        d *= i
    return d
print(factorial(4))

print(f(4))



data = "kayak"

def p(data, i):
    if data[i] != data[-1-i]:
        return False
    if len(data) // 2 == i:
        return True
    return p(data, i+1)

print(p("kayek", 0))


def r(n):
    print(n)
    if n == 1:
        return n
    elif n % 2 != 0:
        return r(3 * n + 1)
    else: return r(n // 2)

r(3)


def r2(n):
    if n == 3:
        return 4
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    else: return r2(n-1) + r2(n-2) + r2(n - 3)

print(r2(5))