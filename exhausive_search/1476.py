import sys

year = list(map(int, sys.stdin.readline().strip().split()))
e = 15
s = 28
m = 19
current = 1

while (current - year[0]) % e != 0 or (current - year[1]) % s != 0 or (current - year[2]) % m != 0:
    current += 1

print(current)