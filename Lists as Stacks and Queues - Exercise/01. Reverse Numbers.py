numbers = input().split()
length = len(numbers)
print(' '.join([numbers.pop() for _ in range(length)]))


