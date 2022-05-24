expression = input()
brackets = []

for i in range(len(expression)):
    if expression[i] == '(':
        brackets.append(i)
    elif expression[i] == ')':
        start, stop = brackets.pop(), i + 1
        print(expression[start: stop])

















