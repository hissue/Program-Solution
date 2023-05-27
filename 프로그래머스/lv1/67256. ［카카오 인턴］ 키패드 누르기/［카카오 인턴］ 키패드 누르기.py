def check(hand,n):
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == hand:
                result_hand = (i,j)
            if keypad[i][j] == n:
                cur_result = (i,j)
    
    return abs(result_hand[0]-cur_result[0]) + abs(result_hand[1]-cur_result[1])

def solution(numbers, hand):
    answer = []
    L_hand = '*'
    R_hand = '#'
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer.append('L')
            L_hand = n
        elif n == 3 or n == 6 or n == 9:
            answer.append('R')
            R_hand = n
        else:
            L_hand_result = check(L_hand,n)
            R_hand_result = check(R_hand,n)
            # 뭐가 더 가까운지 계산하는 공식 필요
            if L_hand_result > R_hand_result:
                answer.append('R')
                R_hand = n
            elif L_hand_result < R_hand_result:
                answer.append('L')
                L_hand = n
            else:
                if hand == 'right':
                    answer.append('R')
                    R_hand = n
                else:
                    answer.append('L')
                    L_hand = n

    return ''.join(answer)

# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))