str = 'Dong2Go'

def fun(ss,n):
    for i in range(n):
        ll = list(ss)
        nn = len(ss)
        s = ll[nn-1]
        while(nn != 0):
            ll[nn-1] = ll[nn-2]
            nn -= 1 
        ll.pop(0)   
        ll = [s] + ll
        ss = ''.join(ll)
    return ss

res = fun(str,3)
print(res)