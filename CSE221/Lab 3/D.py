import sys
MOD = 10**9 +     7

def mat_mult(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            result[i][j] %= MOD
    return result
    # return [
    #     [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
    #      (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
    #     [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
    #      (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    # ]

def mat_pow(matrix, power):
    result = [[1, 0], [0, 1]]
    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, matrix)
        matrix = mat_mult(matrix, matrix)
        power//=2
    return result

T = int(sys.stdin.readline().strip())
for i in range(T):
    a11, a12, a21, a22 = map(int, sys.stdin.readline().split())
    X = int(sys.stdin.readline().strip())
    A = [[a11, a12], [a21, a22]]
    res = mat_pow(A, X)
    print(res[0][0], res[0][1])
    print(res[1][0], res[1][1])
