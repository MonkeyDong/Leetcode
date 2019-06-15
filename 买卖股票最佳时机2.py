class Solution:
    def maxProfit(self, prices):
        sta = 0
        res = 0
        buy = 0
        sell = 0
        nn = len(prices)
        for i in range(nn-1):
            if sta ==0 and prices[i] < prices[i+1]:
                buy = prices[i]
                sta = 1
            elif sta == 1 and prices[i] >= prices[i+1]:
                sell = prices[i]
                sta = 0
                res = res+sell-buy
        if sta == 0 and sell == 0:
            return 0
        if sta == 1:
            return res+prices[nn-1]-buy
        return res

A = Solution()
print(A.maxProfit([7,1,5,3,6,4]))