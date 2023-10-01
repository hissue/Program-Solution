def solution(arr, query):
    answer = []
    for idx in range(len(query)):
        #짝수
        if not idx%2:
            arr = arr[:query[idx]+1]
        #홀수
        else:
            arr = arr[query[idx]:]
    return arr