from sys import stdin
import sys
input = sys.stdin.readline
l = list(map(int, input().split()))
cnt = 0

blue = l[0]
red = 0
b = l[1]
c = l[2]
d = l[3]

if b >= c * d:
    print(-1)
else:
    while True:
        red += c
        blue += b
        cnt += 1
        if blue <= red * d:
            break
    print(cnt)