from collections import deque

water = int(input())
people = deque()

while True:
    text = input()
    if text == 'Start':
        break
    people.append(text)

while True:
    command = input()
    if command == 'End':
        break
    elif command.isdigit():
        person = people.popleft()
        if int(command) <= water:
            water -= int(command)
            print(f"{person} got water")
        else:
            print(f"{person} must wait")
    elif command.startswith("refill "):
        liters = command.split()
        water += int(liters[1])

print(f"{water} liters left")


