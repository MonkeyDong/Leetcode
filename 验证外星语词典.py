class Solution:
    def isAlienSorted(self, words, order):
        dic = {x:ind for ind,x in enumerate(order)}
        t = 1
        i = 0
        nn = len(words)
        while(t == 1 and i < nn):
            ss = []
            for j in words[i]:
                ss.append(dic[j])
            if ss != sorted(ss):
                t = 0
            i += 1
        if t == 1:
            return True
        else:
            return False


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print('-------------------leetcode---------------------')
leetcode = Solution()
res = leetcode.isAlienSorted(words,order)
print(res)




