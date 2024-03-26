# 중위표현 수식 --> 후위표현 수식

def solution(S):
    opStack = ArrayStack()
    
    result = ""
    
    for i in S:
        if prec.get(i, 0) != 0:
            if opStack.isEmpty() or i == "(":
                opStack.push(i)
            else:
                while not opStack.isEmpty() and prec[opStack.peek()] >= prec[i]:
                    result += opStack.pop()
                    
                opStack.push(i)
        else:
            if i != ")":
                result += i
            else:
                while opStack.peek() != "(":
                    result += opStack.pop()
                    
                opStack.pop()
                
    while not opStack.isEmpty():
        result += opStack.pop()
            
    return result