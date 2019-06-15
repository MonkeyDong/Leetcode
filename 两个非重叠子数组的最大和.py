class Solution:
    def maxSumTwoNoOverlap(self, A, L, M):
        lsum = {}
        msum = {}
        for i in range(len(A)-L+1):
            if i == 0:
                lsum[i] = sum(A[:L])
            else:
                lsum[i] = lsum[i-1] - A[i-1] + A[i+L-1]

        for i in range(len(A) - M + 1):
            if i == 0:
                msum[i] = sum(A[:M])
            else:
                msum[i] = msum[i-1] - A[i-1] + A[i+M-1]

        res = 0
        for i in range(0,len(A)-L+1):
            if i > len(A) - M:
                break
            for j in range(i+L,len(A)-M+1):
                res = max(res,lsum[i]+msum[j])

        for j in range(0,len(A)-M+1):
            if j > len(A) - L:
                break
            for i in range(j+M,len(A)-L+1):
                res = max(res,lsum[i]+msum[j])

        return res


A = [2,1,5,6,0,9,5,0,3,8]
L = 4
M = 3
Leetcode = Solution()
res = Leetcode.maxSumTwoNoOverlap(A,L,M)
print(res)
