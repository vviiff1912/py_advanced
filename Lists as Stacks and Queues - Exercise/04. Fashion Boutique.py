clothes_stack = [int(el) for el in input().split()]
rack_capacity = int(input())
capacity = 0
racks = 0

while clothes_stack:
    current_clothes = clothes_stack.pop()

    if current_clothes <= rack_capacity - capacity:
        capacity += current_clothes
        if not clothes_stack:
            racks += 1
            break
        continue

    racks += 1
    capacity = 0
    clothes_stack.append(current_clothes)

print(racks)

