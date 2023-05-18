from itertools import combinations_with_replacement
def solution(n, info):
    max_score = [-1]
    max_gap = -1
    scores = [0,1,2,3,4,5,6,7,8,9,10]
    # 1. 나올 수 있는 스코어의 모든 경우의 수 찾기
    for score in combinations_with_replacement(scores,n):
        score_board = [0 for i in range(11)]
        # 2. 해당 스코어 저장
        for s in score:
            score_board[10-s] += 1

        # 3. 어피치 점수와 비교 (0이 아닌 경우)
        lion = 0
        appeach = 0
        for i in range(11):
            ## 3-1. 라이언 == 어피치 => 어피치
            if score_board[i] == 0 and info[i] == 0:
                continue
            ## 3-2. 라이언 > 어피치
            elif score_board[i] > info[i]:
                lion+=(10-i)
            ## 3-3. 라이언 < 어피치, 라이언 == 어피치
            else:
                appeach+=(10-i)
        
        # 4. 라이언 > 어피치 (갭 차이 확인)
        if lion > appeach:
            gap = lion - appeach
            if gap > max_gap:
                max_gap = gap
                max_score = score_board
        ## 4-2. max_gap 보다 gap이 크다면 max_gap = gap, max_board = score_board
    return max_score