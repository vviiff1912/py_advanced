from collections import deque

people = deque()

while True:
    text = input()
    if text == 'End':
        break
    elif text == 'Paid':
        while people:
            print(people.popleft())
    else:
        people.append(text)

print(f"{len(people)} people remaining.")

