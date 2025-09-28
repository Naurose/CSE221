import sys
T = int(sys.stdin.readline().strip())
outputs = []

for i in range(T):
    values = sys.stdin.readline().strip().split()
    num1, sign, num2 = int(values[1]), values[2], int(values[3])

    if sign == "+":
        result = num1 + num2
    elif sign == "-":
        result = num1 - num2
    elif sign == "*":
        result = num1 * num2
    elif sign == "/":
        result = num1 / num2
    outputs.append(f"{result:.6f}")

sys.stdout.write("\n".join(outputs)+"\n")
