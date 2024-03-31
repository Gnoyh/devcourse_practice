# 카펫

def solution(brown, red):
    for i in range(3, int((brown + red) ** 0.5) + 1):
        if i * (brown // 2 - i + 2) == brown + red:
            return [brown // 2 - i + 2, i]