# 운송 트럭

def solution(max_weight, specs, names):
    result = 0
    
    specs_dict = {}
    
    for i in specs:
        specs_dict[i[0]] = int(i[1])
        
    check = 0
    
    for i in names:
        if check + specs_dict[i] > max_weight:
            result += 1
            check = specs_dict[i]
        else:
            check += specs_dict[i]
            
    return result + 1