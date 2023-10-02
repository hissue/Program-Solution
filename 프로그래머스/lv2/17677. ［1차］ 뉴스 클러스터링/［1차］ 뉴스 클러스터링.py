import collections, math
def solution(str1, str2):
    A = []
    B = []
    rest = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    for s in range(len(str1)-1):
        temp = str1[s:s+2].strip()
        if temp.isalpha() and len(temp) == 2:
            A.append(temp)
            
    for s in range(len(str2)-1):
        temp = str2[s:s+2].strip()
        if temp.isalpha() and len(temp) == 2:
            B.append(temp)
    
    temp1 = collections.Counter(A)
    temp2 = collections.Counter(B)
    
    for v in (temp1-temp2).values():
        rest+=v

    return 65536 if not A and not B else math.trunc(((len(A) - rest) / (len(B) + rest))*65536)
