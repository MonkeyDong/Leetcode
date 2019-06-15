
def fun(num):
    arr = []
    n = 1
    nn = 1
    while(nn < num):
        arr.append(nn)
        n += 1
        nn = n * n
    res = []
    def bfs(tar,ll,tmp):
        if tar == 0:
           res.append(tmp)
        else:
            for i in ll:
                if tar >= i:
                    bfs(tar-i,ll,tmp+[i])

    bfs(num,arr,[])
    mins = num
    for k in res:
        if len(k) < mins:
            mins = len(k)
            ss = k
    return mins,ss

num = 12
print(fun(num))