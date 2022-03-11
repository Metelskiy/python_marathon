def toPostFixExpression(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = []
    postfixList = []

    for token in infixexpr:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token.isnumeric():
            postfixList.append(token)
        elif token == "(":
            opStack.append(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (len(opStack) != 0) and (prec[opStack[-1]] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.append(token)

    while len(opStack) != 0:
        postfixList.append(opStack.pop())
    return postfixList
a=["2","+","3"]
e=["20","+","3","*","(","5", "*","4",")"]
print(toPostFixExpression(e))
# while (not opStack==False) and \