class Solution:
    global res
    res = []
    def Permutation(self,ss):
        global res
        if ss == "":
            return []
        n = len(ss)
        vis = [0 for i in range(n)]
        strs = []
        res = []
        self.DFS(vis,ss,strs,n)
        for i in range(len(res)):
            res[i] = "".join(res[i])
        res = list(set(res))
        return sorted(res)

    def DFS(self,vis,ss,strs,n):
        global res
        if len(strs) == n:
            l = strs[::1]
            res.append(l)
            return
        for i in range(n):
            if vis[i] == 0:
                vis[1] = 1
                strs.append(ss[i])
                self.DFS(vis,ss,strs,n)
                vis[i] = 0
                strs.pop()
        return res


A = Solution()
r = A.Permutation('abc')
print(r)