def solution(land):
    # 행 계산
    for i in range(1,len(land)):
        # 열 계산
        for j in range(4):
            land[i][j]+=max(land[i-1][:j]+land[i-1][j+1:])

    return max(land[-1])