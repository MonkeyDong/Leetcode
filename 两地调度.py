class Solution:
    def twoCitySchedCost(self, costs):
        costs = sorted(costs,key = lambda x:abs(x[0]-x[1]),reverse = True)
        sum = 0
        a1 = 0
        a2 = 0
        n = len(costs)//2
        for i in costs:
            c = min(i)
            ic = i.index(c)
            if a1 < n and ic == 0:
                sum += c
                a1 += 1
            elif a2 < n and ic == 1:
                sum += c
                a2 += 1
            elif (a1 >= n and ic == 0) or (a2 >= n and ic == 1):
                sum += max(i)
            elif (a1 >= n and ic == 1) or (a2 >= n and ic == 0):
                sum += min(i)
        return sum

arrs = [[10,20],[30,200],[400,50],[30,20]]
Leetcode = Solution()
res = Leetcode.twoCitySchedCost(arrs)
print(res)