from collections import deque

number_pumps = int(input())
petrol_pumps = deque()
position = None
petrol_left = 0

for index in range(number_pumps):
    petrol, distance = input().split()
    petrol_pumps.append([index, int(petrol), int(distance)])

while True:
    current_pump = petrol_pumps.popleft()

    if position == current_pump[0]:
        break
    if position is None:
        position = current_pump[0]

    petrol, distance = current_pump[1], current_pump[2]

    if (petrol + petrol_left) >= distance:
        petrol_left = (petrol + petrol_left) - distance
        petrol_pumps.append([position, petrol, distance])
        continue
    petrol_pumps.append([position, petrol, distance])
    position = None
    petrol_left = 0

print(position)





