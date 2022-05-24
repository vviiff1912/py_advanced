from collections import deque

kids = deque(input().split())
toss = int(input())

count = 0

while len(kids) > 1:
    count += 1
    if count == toss:
        kid = kids.popleft()
        print(f"Removed {kid}")
        count = 0
        continue
    kids.append(kids.popleft())

print(f"Last is {kids.popleft()}")


