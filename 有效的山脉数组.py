class Solution:
    def validMountainArray(self, A):
        nn = len(A)
        p = 0
        q = nn-1

        if nn < 3:
            return Fasle
        while q-1 >= 0 and A[q] < A[q-1]:
            q -= 1
        while p+1 <= nn-1 and A[p+1] > A[p]:
            p += 1
        if p > 0 and q < nn-1 and p ==q:
            return True
        else:
            return False

leet = Solution()
res = leet.validMountainArray([1,1,2,2,1,0])
print(res)