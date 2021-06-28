from sys import stdin
import sys
input = sys.stdin.readline
l = list(map(int, input().split()))
sl = sorted(l)
print(sl[2]+ sl[1])