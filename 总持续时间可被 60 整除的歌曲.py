from collections import Counter
class Solution:
    def numPairsDivisibleBy60(self, time):
        cnt = Counter()
        res = 0
        for t in time: 
            res += cnt[-t % 60]#trick
            cnt[t % 60] += 1
        return res


leetcode = Solution()
res = leetcode.numPairsDivisibleBy60([60,60,60])
print(res)
