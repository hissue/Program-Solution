def solution(k, tangerine):
    answer = []
    # 크기 중복 귤 구하기
    box = {}
    for i in tangerine:
        if i in box:
            box[i] += 1
        else:
            box[i] = 1

    # 재정렬
    for j in box.keys():
        answer.append(box[j])
    answer.sort(reverse=True)

    # count
    cnt = 0
    while k > 0:
        k -= answer.pop(0)
        cnt += 1
    return cnt