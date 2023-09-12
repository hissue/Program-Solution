import sys
# def permutation(arr, n):
#     result = []
#     if n == 0:
#         return [[]]
    
#     for i in range(len(arr)):
#         elem = arr[i]
#         for rest in permutation(arr[:i+1] + arr[i+1:], n - 1):
#             result.append([elem] + rest)
#     return result
    

# n = int(sys.stdin.readline())
# k = int(sys.stdin.readline())
# arr = [sys.stdin.readline().rstrip() for _ in range(n)]
# sol = []
# for i in permutation(arr,k):
#     sol.append(''.join(i))
# print(len(set(sol)))

#백트래킹
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = [sys.stdin.readline().rstrip() for i in range(n)]

s = []
result = set()
def dfs():
    
    if len(s) == k:
        temp = ''
        for _ in s:
            temp+=arr[_]
        result.add(temp)
        return 
    
    for i in range(len(arr)):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

dfs()
print(len(result))