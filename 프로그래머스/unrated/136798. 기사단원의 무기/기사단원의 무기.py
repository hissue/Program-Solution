def get_divisor(n):
    data = set()

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            data.add(i)
            data.add(n // i)
    return len(data)

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        result = get_divisor(i)
        if result > limit:
            answer+=power
        else:
            answer+=result
    return answer