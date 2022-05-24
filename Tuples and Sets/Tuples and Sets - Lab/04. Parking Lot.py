plate_numbers = set()

for _ in range(int(input())):
    action, plate_number = input().split(', ')
    if action == 'IN':
        plate_numbers.add(plate_number)
    elif action == 'OUT':
        plate_numbers.remove(plate_number)

if len(plate_numbers) == 0:
    print("Parking Lot is Empty")
else:
    [print(el) for el in plate_numbers]

