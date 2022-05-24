num = int(input()) + 1
odd = set()
even = set()


for i in range(1, num):
    name = input()
    result = sum(ord(letter) for letter in name) // i
    if result % 2 == 0:
        even.add(result)
    else:
        odd.add(result)

if sum(odd) == sum(even):
    result = odd.union(even)
elif sum(odd) > sum(even):
    result = odd.difference(even)
else:
    result = even.symmetric_difference(odd)
print(', '.join([str(el) for el in result]))


