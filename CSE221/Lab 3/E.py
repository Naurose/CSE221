#E
import sys 
def fast_series(a, n, m):
    if a == 1:
        return n % m
    
    mod = m * (a - 1)
    result = 1
    base = a
    power = n + 1

    while power > 0:
        if power % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        power //= 2
    
    divisor = a - 1
    return ((result - a) // divisor) % m

T = int(sys.stdin.readline())
for _ in range(T):
    a, n, m = map(int, sys.stdin.readline().split())
    print(fast_series(a, n, m))
