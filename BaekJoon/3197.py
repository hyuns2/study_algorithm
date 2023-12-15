# 백조의 호수

import sys
from collections import deque

# sys.stdin = open("in.txt", "r")

def check1(x, i, j, swan, next, visited, ifWater):
    if x >= 0 and visited[i][j] == False:
        if lake[i][j] == '.':
            swan.append([i, j])
        else:
            next.append([i, j])
            if ifWater == 1:
                lake[i][j] = '.'
        visited[i][j] = True

def check2(x, n, i, j, swan, next, visited, ifWater):
    if x < n and visited[i][j] == False:
        if lake[i][j] == '.':
            swan.append([i, j])
        else:
            next.append([i, j])
            if ifWater == 1:
                lake[i][j] = '.'
        visited[i][j] = True

def search():
    while swan.__len__() != 0:
        temp = swan.popleft()
        i = temp[0]
        j = temp[1]

        if i == swans[1][0] and j == swans[1][1]:
            return 1

        check1(i - 1, i - 1, j, swan, snext, svisited, 0)
        check1(j - 1, i, j - 1, swan, snext, svisited, 0)
        check2(i + 1, n, i + 1, j, swan, snext, svisited, 0)
        check2(j + 1, m, i, j + 1, swan, snext, svisited, 0)

    return -1

def melt():
    while water.__len__() != 0:
        temp = water.popleft()
        i = temp[0]
        j = temp[1]

        check1(i - 1, i - 1, j, water, wnext, wvisited, 1)
        check1(j - 1, i, j - 1, water, wnext, wvisited, 1)
        check2(i + 1, n, i + 1, j, water, wnext, wvisited, 1)
        check2(j + 1, m, i, j + 1, water, wnext, wvisited, 1)

# main
n, m = map(int, sys.stdin.readline().split())

lake = []
swans = []
svisited = [[False for i in range(m)] for j in range(n)]
wvisited = [[False for i in range(m)] for j in range(n)]
swan = deque()
water = deque()
snext = deque()
wnext = deque()

for i in range(n):
    rowLine = sys.stdin.readline().rstrip()
    row = list(rowLine)
    for j in range(m):
        if row[j] == 'L':
            swans.append([i, j])
            row[j] = '.'
        if row[j] == '.':
            water.append([i, j])
    lake.append(row)

swan.append(swans[0])
svisited[swans[0][0]][swans[0][1]] = True

date = 0
temp = search()

while temp != 1:
    melt()
    date += 1
    swan = snext
    water = wnext
    snext = deque()
    wnext = deque()
    temp = search()

print(date)