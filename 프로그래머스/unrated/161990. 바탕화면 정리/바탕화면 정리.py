def solution(wallpaper):
    a = []
    b = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                a.append(i)
                b.append(j)
                
    lux = min(a)
    rdx = max(a)+1
    luy = min(b)
    rdy = max(b)+1
    return [lux,luy,rdx,rdy]