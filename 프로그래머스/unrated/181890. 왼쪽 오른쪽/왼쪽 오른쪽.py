def solution(str_list):
    for idx,data in enumerate(str_list):
        if data == "l":
            return str_list[:idx]
        elif data == "r":
            return str_list[idx+1:]
    return []
