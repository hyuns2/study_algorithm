import sys

s = int(sys.stdin.readline().strip())

table = [-1 for _ in range(s+1)]
table[0] = 0
table[1] = 0
if s > 1:
    table[2] = 1
if s > 2:
    table[3] = 1

def func(n):
    if n <= 1:
        return 0

    result = s
    if n % 3 == 0:
        temp = n // 3
        if table[temp] != -1:
            result = min(result, 1 + table[temp])
        else:
            result = min(result, 1 + func(temp))
    if n % 2 == 0:
        temp = n // 2
        if table[temp] != -1:
            result = min(result, 1 + table[temp])
        else:
            result = min(result, 1 + func(temp))
    if table[n - 1] != -1:
        result = min(result, 1 + table[n - 1])
    else:
        result = min(result, 1 + func(n - 1))

    return result

for i in range(4, s+1):
    table[i] = func(i)

print(table[s])