from collections import deque


numbers = deque(sorted(list(map(int, input().split()))))
target = int(input())

iterations = 0
summation_pairs = set()
temporary_summation_pair = set()
length = len(numbers)
number = numbers.popleft()

for _ in range(length - 1):
    for i in range(length - 1):
        iterations += 1
        current_num = numbers[i]
        if number + current_num == target:
            pair_as_str = (number, current_num)
            if pair_as_str not in temporary_summation_pair:
                summation_pairs.add(pair_as_str)
                temporary_summation_pair.add(pair_as_str)
                print(f"{number} + {current_num} = {target}")

    numbers = deque(numbers)
    numbers.append(number)
    number = numbers.popleft()
    temporary_summation_pair.clear()
a = 7
print(f"Iterations done: {iterations}")
[print(f"({element1}, {element2})") for element1, element2 in summation_pairs]
