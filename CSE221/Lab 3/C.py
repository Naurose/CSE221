#C #Fast Power Drift
import sys
def power_drift(a, b):
    output = 1
    while b > 0:
        if b%2 == 1:
            output = a*output % 107
        a = a*a % 107
        b = b//2
    return output
a, b = map(int, sys.stdin.readline().split())
print(power_drift(a, b))