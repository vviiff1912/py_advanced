numbers = [float(num) for num in input().split()]
numbers_count = {}

for num in numbers:
    if num not in numbers_count.keys():
        numbers_count[num] = numbers.count(num)
        print(f"{num} - {numbers_count[num]} times")
