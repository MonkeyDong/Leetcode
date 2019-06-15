class Solution:
    def hasGroupsSizeX(self, deck):
        tmp = set(deck)
        dic = {x:0 for x in tmp}
        for i in deck:
            dic[i] += 1
        c = min(set(dic.values()))
        if c < 2:
            return False
        def fun(x,y):
            for i in range(1,y+1):
                if (x%i == 0) and (y%i == 0):
                    hcf = i
            if hcf >= 2:
                return True
            return False
        for i in set(dic.values()):
            if not fun(i,c):
                return False
        return True

arr = [1,2,3,4,4,3,2,1]
a = Solution()
res = a.hasGroupsSizeX(arr)
print(res)