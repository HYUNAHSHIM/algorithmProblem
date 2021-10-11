# BaekJoon1927.py

import sys
import heapq

input = sys.stdin.readline
number = int(input())
heap = []

for _ in range(number):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)