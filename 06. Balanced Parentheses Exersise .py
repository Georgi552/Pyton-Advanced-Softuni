expresion = input()
stack = []
balaced = True
for el in expresion:
    if el in "({[":
        stack.append(el)
    elif el in ")}]":
        if len(stack) == 0:
            balaced = False
            break
        opening_paren = stack.pop()
        if el == ")" and opening_paren == "(":
            continue
        if el == "}" and opening_paren == "{":
            continue
        if el == "]" and opening_paren == "[":
            continue

        else:
            balaced = False
            break
if balaced:
    print("YES")
else:
    print('NO')


