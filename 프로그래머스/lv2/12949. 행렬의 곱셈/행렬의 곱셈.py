def solution(arr1, arr2):
    x = len(arr1)
    y = len(arr2[0])  # 올바른 변수 y를 설정

    # 결과 행렬 초기화
    answer = [[0 for _ in range(y)] for _ in range(x)]

    # 행렬 곱셈 수행
    for i in range(x):
        for j in range(y):
            temp = 0
            for l in range(len(arr1[0])):  # arr1의 열의 길이를 사용
                temp += arr1[i][l] * arr2[l][j]
            answer[i][j] = temp

    return answer