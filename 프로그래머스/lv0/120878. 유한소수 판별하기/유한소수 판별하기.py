def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def factorization(x):
    d = 2
    answer = []
    while d <= x:
        if x % d == 0:
            answer.append(d)
            x = x / d
        else:
            d = d + 1
    return answer
            
def solution(a, b):
    temp = gcd(a,b)
    answer = factorization(b//temp) 
    for data in answer:
        if data == 2 or data ==5:
            continue
        else:     
            return 2
    return 1