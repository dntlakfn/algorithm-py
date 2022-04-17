def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)




def f_dp(n):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 0
    cache[1] = 1

    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

print(f_dp(40))
print(fibonacci(40))