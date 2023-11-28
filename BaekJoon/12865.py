# 평범한 배낭

def knapsack():
    for j in range(min(W), k+1):
        for i in range(1, n+1):
            if W[i-1] <= j:
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-W[i-1]] + V[i-1])
            else:
                DP[i][j] = DP[i-1][j]

n, k = map(int, input().split())

DP = [[0 for j in range(k+1)] for i in range(n+1)]

W = []
V = []
for i in range(n):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

knapsack()

print(DP[n][k])