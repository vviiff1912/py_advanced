parentheses = input()
parentheses_stack = []
balanced = True

for el in parentheses:
    if el in '{[(':
        parentheses_stack.append(el)
    elif not parentheses_stack:
        balanced = False
        break
    elif el in '}])':
        element = parentheses_stack.pop()
        if el == '}' and element == '{':
            continue
        elif el == ']' and element == '[':
            continue
        elif el == ')' and element == '(':
            continue
        else:
            balanced = False
            break

if balanced and not parentheses_stack:
    print('YES')
else:
    print('NO')
