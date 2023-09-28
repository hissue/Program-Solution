def solution(str_list):
    if  "l" not in str_list and "r" not in str_list:
        return []
    for idx,data in enumerate(str_list):
        if data == "l":
            return str_list[:idx]
        elif data == "r":
            return str_list[idx+1:]
        else:
            continue
            
