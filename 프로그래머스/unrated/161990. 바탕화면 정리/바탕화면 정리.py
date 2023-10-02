def solution(wallpaper):
    index = []
    dic = {}
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                index.append([i,j])
                
    lux = index[0][0]
    rdx = index[-1][0]+1
    temp = sorted(index,key=lambda x : x[-1])
    luy = temp[0][-1]
    rdy = temp[-1][-1]+1
    return [lux,luy,rdx,rdy]