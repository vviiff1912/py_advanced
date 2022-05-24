from collections import deque


def turn_to_hms_time(time, robot_time):
    time_now = time
    time_now %= 24 * 60 * 60
    processing_time = time_now + robot_time
    hours = time // 3600
    time -= hours * 3600
    minutes = time // 60
    time -= minutes * 60
    seconds = time
    if hours == 24:
        hours = 0
    return time_now, processing_time, f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def convert_time_to_seconds(time):
    time = [int(el) for el in time.split(':')]
    return (time[0] * 60 * 60) + (time[1] * 60) + time[2]


robots = {}
products = deque()
robots_busy_until = {}

robots_info = input().split(';')
time = convert_time_to_seconds(input())

while True:
    product_name = input()
    if product_name == 'End':
        break
    products.append(product_name)

for rbt in robots_info:
    name, needed_process_time = rbt.split('-')
    if name not in robots:
        robots[name] = int(needed_process_time)
        robots_busy_until[name] = -1

while products:
    time += 1
    product = products.popleft()
    for robot, process_time in robots_busy_until.items():
        if process_time <= time:
            robot_time = robots[robot]
            time, process_time, current_time = turn_to_hms_time(time, robot_time)
            robots_busy_until[robot] = process_time
            print(f"{robot} - {product} [{current_time}]")
            break
    else:
        products.append(product)

