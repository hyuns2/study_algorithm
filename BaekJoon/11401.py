# 이항계수3

import sys

n, m = map(int, sys.stdin.readline().split())
remainer = 1000000007

top = 1
bottom = 1
for i in range(2, n + 1):
    top = top * i % remainer
    if i == n - m:
        bottom *= top
    if i == m:
        bottom *= top

bottom %= remainer
print(top * pow(bottom, remainer - 2, remainer) % remainer)