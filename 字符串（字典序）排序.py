lists = ['aab','aad','aac','abc','aba','bba','bab']

def fun(nums,s):
    arr = []
    dic = {}
    for n in nums:
        if n[s] in dic.keys():
            dic[n[s]].append(n)
        else:
            dic[n[s]] = []
            dic[n[s]].append(n)
    for i in dic.keys():
        if len(dic[i]) == 1:
            arr.append(dic[i][0])
        else:
            for j in dic[i]:
                if len(j) == s+1:
                    arr.append(j)
                    dic[i].remove(j)
            ss = fun(dic[i],s+1)
            for k in ss:
                arr.append(k)
    return arr

res = fun(lists,0)
print(res)               
        
    






