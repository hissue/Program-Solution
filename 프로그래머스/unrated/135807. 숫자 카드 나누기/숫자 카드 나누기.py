def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(arrayA, arrayB):
    a = arrayA[0]
    for i in range(1, len(arrayA)):
        a = gcd(a, arrayA[i])

    b = arrayB[0]
    for i in range(1, len(arrayB)):
        b = gcd(b, arrayB[i])

    for i in range(len(arrayA)):
        if arrayA[i] % b == 0:
            b = 1
        if arrayB[i] % a == 0:
            a = 1
    
    if a == 1 and b == 1:
        return 0
    else:
        return max(a,b)