def solution(id_list, report, k):
#     answer = {}
#     result = {}
#     total = [0] * len(id_list)
#     for data in report:
#         a,b = data.split(" ")
#         if b not in result:
#             result[b] = 0
            
#         if a not in answer:
#             answer[a] = [b]
#             result[b] +=1  
#         else:
#             if b not in answer[a]:   
#                 answer[a].append(b)
#                 result[b] +=1
        
#     for myKey, datas in answer.items():
#         for data in datas:
#             if result[data] >= k:
#                 total[id_list.index(myKey)] +=1

    answer = [0] * len(id_list)
    reports = {}
    for r in set(report):
        a,b = r.split(" ")   
        if b not in reports:
            reports[b] = 1
        else:  
            reports[b] += 1
    
    for r in set(report):
        a,b = r.split(" ")
        if reports[b] >= k:
            answer[id_list.index(a)] +=1
    
    return answer