def solution(number, limit, power):
    answer = 0
    for n in range(1,number+1):
        data = set()

        for i in range(1, int(n ** (1 / 2)) + 1):
            if n % i == 0:
                data.add(i)
                data.add(n // i)
                
            if len(data) > limit:
                break
                
        result = len(data)
        
        if result > limit:
            answer+=power
        else:
            answer+=result
            
    return answer