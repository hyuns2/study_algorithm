# 가운데를 말해요

import sys
import heapq

def pushAndFindMid(data):
    if maxHeap.__len__() == minHeap.__len__():
        heapq.heappush(maxHeap, data * -1)
    else:
        heapq.heappush(minHeap, data)

    if minHeap.__len__() > 0 and maxHeap[0] * -1 > minHeap[0]:
        maxData = heapq.heappop(maxHeap) * -1
        minData = heapq.heappop(minHeap) * -1
        heapq.heappush(maxHeap, minData)
        heapq.heappush(minHeap, maxData)

    result.append(maxHeap[0] * -1)

maxHeap = []
minHeap = []
result = []

n = int(input())
for i in range(n):
    data = int(sys.stdin.readline())
    pushAndFindMid(data)

for i in range(result.__len__()):
    print(result[i])