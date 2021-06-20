import sys
input = sys.stdin.readline
import collections

n = int(input())
l_a = list(map(int, input().split()))
all = n*(n-1)/2

c = collections.Counter(l_a)
ll = list(c.values())
#l_b = sorted(l_a)
#l_c = list(set(l_b))
#ll = []

#for i in l_c:
#  cnt = 0
#  for j in l_b:
#    if i == j:
#      cnt += 1
#  ll.append(cnt)

cc = 0
for i in ll:
  cc += i * (i-1)/2

print(int(all - cc))
