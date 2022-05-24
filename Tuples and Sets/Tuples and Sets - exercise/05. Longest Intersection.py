num = int(input())
# first = set()
# second = set()
result = set()

for _ in range(num):
    ranges = input().split('-')
    range1 = [int(n) for n in ranges[0].split(',')]
    range2 = [int(k) for k in ranges[1].split(',')]

    # for i in range(range1[0], range1[1] + 1):
    #     first.add(i)
    # for j in range(range2[0], range2[1] + 1):
    #     second.add(j)
    first = set(range(range1[0], range1[1] + 1))
    second = set(range(range2[0], range2[1] + 1))
    current_result = first.intersection(second)
    if len(current_result) > len(result):
        result = current_result
    first = set()
    second = set()

print(f"Longest intersection is [{', '.join([str(el) for el in result])}] with length {len(result)}")

