from sys import stdin
import sys
input = sys.stdin.readline
import math
p = int(input())
l = []
n = 9
for i in range(10):
    l.append(math.factorial(i+1))
for i in range(1, 10):
    if l[i] > p:
        n = i-1
        break
    else:
        continue
cnt = 0
while True:
    if p >= l[n]:
        tmp = p // l[n]
        cnt += tmp
        p = p % l[n]
        if p == 0:
            break
    else:
        n -= 1

print(cnt)