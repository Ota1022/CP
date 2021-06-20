import sys
input = sys.stdin.readline
n = int(input())

money = 0
cnt = 0
adn = 1
while True:
  if money < n:
    money += adn
    adn += 1
    cnt += 1
  else:
    print(cnt)
    break
    