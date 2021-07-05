from sys import stdin
import sys
input = sys.stdin.readline

def solve():
    from sys import stdin
    import sys
    input = sys.stdin.readline
    a, b, c = map(int, input().split())
    import math

    if c % 2 == 1:
        if a < b:
            return "<"
        elif a > b:
            return ">"
        else:
            return "="
    else:
        if abs(a) < abs(b):
            return "<"
        elif abs(a) > abs(b):
            return ">"
        else:
            return "="

print(solve())