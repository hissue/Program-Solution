import collections
def solution(X, Y):
    countX = collections.Counter(X)
    countY = collections.Counter(Y)
    answer = (countX + countY) - (countX - countY) - (countY - countX)
    if not answer.keys():
        return "-1"
    elif len(answer.keys()) == 1 and list(answer.keys())[0] == "0":
        return "0"    
    else:
        result = []
        for k,v in answer.items():
            result.append(k*(v//2))
        return "".join(sorted(result, reverse=True))
