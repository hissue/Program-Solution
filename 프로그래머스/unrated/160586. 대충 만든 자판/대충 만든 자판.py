def solution(keymap, targets):
    answer = {}
    result = []
    for idx in range(len(keymap)):
        for idx, key in enumerate(keymap[idx]):
            if key in answer:
                answer[key] = min(answer[key],idx+1)
            else:
                answer[key] = idx+1
    
    for target in targets:
        count = 0
        for key in target:
            if key in answer.keys():
                count += answer[key]
            else:
                count = -1
                break
        result.append(count)
    return result