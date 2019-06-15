class Solution:
    def fun(self,s):
        if len(s) == 1:
            return True
        ss = s.split()
        strs = ''
        for i in ss:
            x = []
            for j in i:
                if j.isalpha() or j.isdigit():
                    x.append(j.lower())
            xs = ''.join(x)
            strs = ''.join([strs,xs])
        n = int(len(strs)/2)
        print(strs)
        for i,j in zip(strs[:n],list(reversed(strs))[:n]):
            if i != j:
                return False
        return True

st = "0P"
Leetcode = Solution()
res = Leetcode.fun(st)
print(res)