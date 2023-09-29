def giyac(n,m):
    length = min(n,m)
    i=2
    while i < length:
        if not n%i and not m%i:
            n //= i
            m //= i
        else:
            i+=1
    return n,m

def solution(numer1, denom1, numer2, denom2):
    n,m = giyac(((numer1*denom2) + (numer2*denom1)) , (denom1*denom2))
    return [n,m]