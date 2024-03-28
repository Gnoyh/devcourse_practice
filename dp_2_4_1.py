# 완주하지 못한 선수

def solution(participant, completion):
    result_dict = {}
    
    for i in participant:
        result_dict[i] = result_dict.get(i, 0) + 1
    
    for i in completion:
        result_dict[i] -= 1
        
        if result_dict[i] == 0:
            del result_dict[i]
            
    return list(result_dict.keys())[0]