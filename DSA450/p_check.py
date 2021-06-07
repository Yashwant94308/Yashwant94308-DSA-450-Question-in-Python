s = '(][)'


def p_C():
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == ']' and stack[-1] == '[':
            stack.pop()
        elif i == '}' and stack[-1] == '{':
            stack.pop()
        elif i == ')' and  stack[-1] == '(':
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        return True
    else:
        return False
print(p_C())
