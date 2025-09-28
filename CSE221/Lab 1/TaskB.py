import sys
outputs = []
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    is_asc = True
    is_desc = True
    for i in range(n-1):
        if a[i] > a[i+1]:
            is_asc = False
        if a[i] < a[i+1]:
            is_desc = False

    if is_asc:
        outputs.append("ASCENDING")
    elif is_desc:
        outputs.append("DESCENDING")
    else:
        outputs.append("NO")

sys.stdout.write('\n'.join(outputs))
sys.stdout.flush()
exit(0)