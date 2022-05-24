n = int(input())
number_stack = []

for _ in range(n):
    command = input().split()
    if command[0] == '1':
        number = command[1]
        number_stack.append(number)
    elif command[0] == '2':
        if number_stack:
            number_stack.pop()
    elif command[0] == '3':
        int_number_stack = [int(el) for el in number_stack]
        if int_number_stack:
            print(max(int_number_stack))
    elif command[0] == '4':
        int_number_stack = [int(el) for el in number_stack]
        if int_number_stack:
            print(min(int_number_stack))

length = len(number_stack)
final = []

while number_stack:
    final.append(number_stack.pop())
print(', '.join(final))
