def solution(strings, n):
    # answer = [[] for _ in range(26)]
    # result = []
    # for word in strings:
    #     answer[ord(word[n])%ord("a")].append(word)
    # for data in answer:
    #     if data:
    #         result.extend(sorted(data))
    # return result
    return sorted(strings, key=lambda x : [x[n], x])