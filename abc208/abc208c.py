from sys import stdin
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
id = list(map(int, input().split()))

s_id =sorted(id)
dic = {}
for i in range(n):
    dic[s_id[i]] = i + 1
rest = k % n
cnt = k // n
for i in range(n):
    if dic[id[i]] <= rest:
        print(cnt + 1)
    else:
        print(cnt)

# index = list(range(n)) 
# l = list(zip(id, index))
# l.sort(key = lambda x: x[1])
# cnt = k // n
# rest = k % n
# cnt_l = [cnt] * n

# for i in range(rest):
#     cnt_l[i] = cnt + 1

# if k > n:
#     s_id = sorted(id)
#     ans_l =  list(zip(cnt_l, s_id))


# for i in range(n):
#     x = l[i][0]
#     for j in range(n):
#         if ans_l[j][1] == x:
#             print(ans_l[j][0])