from collections import deque


def passing_by_green(cars, green_l, space):
    crashed = True
    passed_autos = 0
    green_light = green_l + space

    while cars:
        auto_name = cars.popleft()

        if space >= green_light:
            cars.append(auto_name)
            break
        if len(auto_name) <= green_light:
            green_light -= len(auto_name)
            passed_autos += 1
            continue
        else:
            print('A crash happened!')
            print(f"{auto_name} was hit at {auto_name[green_light]}.")
            crashed = False
            break

    return cars, crashed, passed_autos


green = int(input())
window = int(input())
cars = deque()
everything_ok = True
total_passed_cars = 0

while everything_ok:
    command = input()
    if command == 'END':
        break
    elif command == 'green':
        cars, everything_ok, passed_cars = passing_by_green(cars, green, window)
        total_passed_cars += passed_cars
    else:
        cars.append(command)

if everything_ok:
    print('Everyone is safe.')
    print(f"{total_passed_cars} total cars passed the crossroads.")

