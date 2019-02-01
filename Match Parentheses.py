def match(parentheses):

    table = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    n = len(parentheses)
    stack=[]
    for i in range(0 ,n):
        if parentheses[i]=="(" or parentheses[i]=="{" or parentheses[i]=="[":
            stack.append(parentheses[i])
        elif parentheses[i] in (")", "}", "]"):
            if stack==[]:
                return False
            else:
                top = stack.pop()
                if table[parentheses[i]] != top:
                    return False
    if stack==[]:
        return True
    else:
        return False
print(match("[{()}]"))
