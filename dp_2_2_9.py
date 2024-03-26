# 후위표현 수식 계산

def postfixEval(tokenList):
    calStack = ArrayStack()
    
    for i in tokenList:
        if str(i).isdigit():
            calStack.push(i)
        else:
            sn = calStack.pop()
            fn = calStack.pop()
            
            if i == "+":
                calStack.push(fn + sn)
            elif i == "-":
                calStack.push(fn - sn)
            elif i == "*":
                calStack.push(fn * sn)
            else:
                calStack.push(fn / sn)
                
    return calStack.pop()