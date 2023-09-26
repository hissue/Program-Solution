def solution(a, b):
    months = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    # answer = (sum(months[:a])+b)%7
    # if answer == 1:
    #     return "FRI"
    # elif answer == 2:
    #     return "SAT"
    # elif answer == 3:
    #     return "SUN"
    # elif answer == 4:
    #     return "MON"
    # elif answer == 5:
    #     return "TUE"
    # elif answer == 6:
    #     return "WED"
    # else:
    #     return "THU"
        
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    return week[(sum(months[:a])+b)%7]
