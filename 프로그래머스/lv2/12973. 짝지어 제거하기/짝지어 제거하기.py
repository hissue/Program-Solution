# from collections import deque
# def solution(s):
#     left_list = [s[0]]
#     right_list = deque(s[1:])
    
#     while right_list :
#         if not left_list or left_list[-1] != right_list[0]:
#             left_list.append(right_list.popleft())
#         else:  
#             left_list.pop()
#             right_list.popleft()  
#     return 0 if len(left_list) else 1
def solution(s):
    temp = [" ", s[0]]
    for i in s[1:]:
        if temp[-1] == i:
            temp.pop()
        else:
            temp.append(i)
    return 1 if len(temp) == 1 else 0
