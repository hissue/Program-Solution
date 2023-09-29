def solution(polynomial):
    temp = polynomial.split(" ")
    a=0
    b=0
    for t in temp:
        if t=="+":
            continue
        elif "x" in t:
            if t[:-1]:
                a+=int(t[:-1])
            else:
                a+=1
        else:
            b+=int(t)
    if a and b:
        if a == 1:
            answer = 'x + '+str(b)
        else:
            answer = str(a)+'x + '+str(b)
            
    elif a:
        if a == 1:
            answer = 'x'
        else:  
            answer = str(a)+'x'
    else:
        answer = str(b)
    return answer