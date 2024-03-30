# 나머지 한 점

def solution(v):
    x_list = set()
    y_list = set()
    
    for i in v:
        if i[0] in x_list:
            x_list.remove(i[0])
        else:
            x_list.add(i[0])
        
        if i[1] in y_list:
            y_list.remove(i[1])
        else:
            y_list.add(i[1])
            
    return [x_list.pop(), y_list.pop()]