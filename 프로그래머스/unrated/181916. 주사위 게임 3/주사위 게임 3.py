import collections
def solution(a, b, c, d):
    counts = collections.Counter([a,b,c,d])
    answer = list(counts)
    
    if len(answer) == 1:
        return 1111*answer[0]
    elif len(answer) == 2:
        for k in answer:
            if counts[k] == 2:
                return (answer[0] + answer[1]) * abs(answer[0] - answer[1])
            elif counts[k] == 3:
                p = k
            else:
                q = k
        return (10 * p + q)**2
    elif len(answer) == 3:
        result = []
        for k in answer:
            if counts[k] != 2:
                result.append(k)
        return result[0] * result[1]
    else:
        return min(answer)