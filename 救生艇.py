people = [3,2,2,1]
limit = 3

def fun(p,l):
    nn = 0

    def Sum1(p,l):
        arr = []
        for i in p:
            if i == l:
                arr.append(i)
        return arr

    def Sum2(p,l):
        arr = []
        dic = {}
        for i in p:
            if i in dic.keys():
                arr.append((i,dic[i]))
            else:
                dic[l-i] = i
        return arr

    while(p != []):
        arr2 = Sum2(p,l)
        for ii in arr2:
            a1 = p.index(ii[0])
            a2 = p.index(ii[1])
            del p[a1],p[a2]
            nn += 1
        arr1 = Sum1(p,l)
        for jj in arr1:
            a = p.index(jj)
            del p[a]
            nn += 1
        l -= 1
    
    return nn

print(fun(people,limit))


