def solution(food):
    answer = ""
    for idx in range(len(food)):
        if food[idx]//2 > 0:
            answer+=str(idx)*(food[idx]//2)
    return answer+"0"+answer[::-1]