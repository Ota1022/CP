import math
from sys import stdin
import sys
input = sys.stdin.readline
n = int(input())
if math.floor(n * 1.08) < 206:
    print("Yay!")
elif math.floor(n * 1.08) == 206:
    print("so-so")
elif math.floor(n * 1.08) > 206:
    print(":(")