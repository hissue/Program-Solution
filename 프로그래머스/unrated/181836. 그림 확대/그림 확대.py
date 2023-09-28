def solution(picture, k):
    result = []
    for p in picture:
        answer = ""
        for word in p:
            answer += word*k
        result.extend([answer]*k)
    return result