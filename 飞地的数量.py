import copy

def maze(x,y,M):
    bools = False
    if x == 0 or y == 0 or x == len(M[0])-1 or y == len(M)-1:
        return True
    MM = copy.deepcopy(M)
    MM[x][y] = 2
    if x+1 < len(M[0]) and M[x+1][y] == 1:
        bools = bools or maze(x+1,y,MM)
    if x-1 > -1 and M[x-1][y] == 1:
        bools = bools or maze(x-1,y,MM)
    if y+1 < len(M) and M[x][y+1] == 1:
        bools = bools or maze(x,y+1,MM)
    if y-1 > -1 and M[x][y-1] == 1:
        bools = bools or maze(x,y-1,MM)
    return bools

M=[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
print(maze(2,2,M))

tt = 0
for i in range(len(M[0])):
    for j in range(len(M)):
        if maze(i,j,M):
            continue
        else:
            tt += 1
print(tt)
