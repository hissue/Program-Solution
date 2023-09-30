def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if not mode:
            if code[idx] == "1":
                mode = 1
            elif not idx%2:
                answer+=code[idx]
        else:
            if code[idx] == "1":
                mode = 0
            elif idx%2:
                answer+=code[idx]
    return answer if answer else "EMPTY"