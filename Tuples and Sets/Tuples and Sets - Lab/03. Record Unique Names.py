num = int(input())
names = []

for _ in range(num):
    name = input()
    if name not in names:
        names.append(name)

print('\n'.join(names))


