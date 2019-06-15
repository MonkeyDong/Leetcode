class Solution:
    def fun(self,ii,nn):
        ji = ii
        while(ji < nn):
            ji = ji * ii
            if ji == nn:
                return True
        return False

    def isPerfectSquare(self, num):
        bools = True
        res = False
        i = 2
        while(bools):
            if i*i <= num:
                if self.fun(i,num):
                    bools = False
                    res = True
                i += 1
            else:
                bools = False
        return res

ns = 9
A = Solution()
rr = A.isPerfectSquare(ns)
print(rr)