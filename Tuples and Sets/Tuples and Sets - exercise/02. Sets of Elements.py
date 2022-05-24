sets = [int(num) for num in input().split()]
num = sum(sets)

set1 = set()
set2 = set()

for i in range(num):
    number = int(input())
    if len(set1) < sets[0]:
        set1.add(number)
    if len(set1) <= i:
        set2.add(number)

result = set1.intersection(set2)
[print(num) for num in result]






