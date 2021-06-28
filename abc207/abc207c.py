from sys import stdin
import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
t = [0] * n
l = [0] * n
r = [0] * n
for i in range(n):
    t[i], l[i], r[i] = map(int, input().split())

cnt = 0
nums = []
for i in range(1, n +1):
    nums.append(i)
    
cmb = combinations(nums, 2)

sec = [[] for _ in range(n)]
for i in range(n):
    if t[i] == 1:
        sec[i][0][0] = l[i]
        sec[i][0][1] = r[i]
        sec[i][1] = ["<=", "<="]
    elif t[i] == 2:
        sec[i][0][0] = [l[i], r[i]]
        sec[i][0] =[1] [l[i], r[i]]
        sec[i][1] = ["<=", "<"]
    elif t[i] == 3:
        sec[i][0] = [l[i], r[i]]
        sec[i][0] = [l[i], r[i]]
        sec[i][1] = ["<", "<="]
    elif t[i] == 4:
        sec[i][0] = [l[i], r[i]]
        sec[i][0] = [l[i], r[i]]
        sec[i][1] = ["<", "<"]

for i in range(n):
    lcmb = list(cmb[i]) 
    a = sec[lcmb[0]][0][0]
    b = sec[lcmb[0]][0][1]
    c = sec[lcmb[1]][0][0]
    d = sec[lcmb[1]][0][1]
    p = sec[lcmb[0]][1][0]
    q = sec[lcmb[0]][1][1]
    r = sec[lcmb[1]][1][0]
    s = sec[lcmb[1]][1][1]
    if b<c or d<a:
        pass
    else:
        if a <= c <= b <= d:
            cnt = 1
        elif c <= a <= d <= b:
            cnt = 1
        elif a <= c <= b <= d:
            cnt += 1
        elif a <= c <= d <= b:
            cnt += 1
print(cnt)