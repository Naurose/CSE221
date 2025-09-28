import sys
def k_th_number(K, x):
    high = K*x
    low = 0
    
    while low < high:
        mid = (high+low)//2
        count = mid-mid//x
        if count < K:
            low = mid + 1
        else:
            high = mid
    return low

T= int(sys.stdin.readline())
for i in range(T):
    K, x = map(int, sys.stdin.readline().split())
    print(k_th_number(K, x))