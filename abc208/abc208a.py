from sys import stdin
import sys
input = sys.stdin.readline
a, b = map(int, input().split())
if 6*a >= b and b >= a:
    print('Yes')
else:
    print('No')
