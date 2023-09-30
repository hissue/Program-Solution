def solution(sides):
    sides.sort()
    # 가장긴뱐
    a = sides[1] - (sides[1] - sides[0])
    # 나머지
    b = sum(sides) - sides[1] - 1
    
    return a+b