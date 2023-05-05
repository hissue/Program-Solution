def solution(triangle):
    length = len(triangle)
    triangle[1][0] += triangle[0][0]
    triangle[1][-1] += triangle[0][0]
    for i in range(2,length):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][-1] += triangle[i-1][-1]
        for j in range(1,i):
            triangle[i][j] = max (triangle[i-1][j-1]+triangle[i][j], triangle[i-1][j]+triangle[i][j]) 

    return max(triangle[length-1])