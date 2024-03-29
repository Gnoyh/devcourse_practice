# 여행경로

def solution(tickets):
    routes = {}
    
    for i in tickets:
        routes[i[0]] = routes.get(i[0], []) + [i[1]]
        
    for i in routes:
        routes[i].sort(reverse = True)
        
    stack = ["ICN"]
    path = []
    
    while len(stack) > 0:
        top = stack[-1]
        
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())
            
    return path[: : -1]