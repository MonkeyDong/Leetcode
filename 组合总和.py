arrs = [2,3,5]
tar = 8

class Solution:
    def main(self,arr,tar):
        arr = sorted(arr)
        for i in reversed(arr):
            if i > tar:
                ind = arr.index(i)
                del arr[i]
            if i <= tar:
                break
        Solution.res = []
        self.dfs(tar,arr,[])
        return Solution.res


    def dfs(self,tars,ars,tmps):
        if tars == 0:
            return Solution.res.append(tmps)
        for i in range(len(ars)):
            va = ars[i]
            if va > tars:
                return
            ss = ars[i:] #可重复
            #ss = ars[i+1:] #不可重复
            self.dfs(tars-va,ss,tmps+[va])

leetcode = Solution()
r = leetcode.main(arrs,tar)
print(r)