A = [1,3,5,7]
B = [2,4,6,8,9,10]

class Solution(object):
	def getKth(self,A,B,k):
		lenA = len(A)
		lenB = len(B)
		if lenA > lenB:
			return self.getKth(B,A,k)
		if lenA == 0:
			return B[k-1]
		if k == 1:
			return min(A[0],B[0])
		pa = int(min(k//2,lenA))
		pb = int(k - pa)
		if A[pa-1] <= B[pb-1]:
			return self.getKth(A[pa:],B,pb)
		else:
			return self.getKth(A,B[pb:],pa)

	def findMedianSortedArrays(self,A,B):
		lenA = len(A)
		lenB = len(B)
		if (lenA + lenB) % 2 == 1:
			return self.getKth(A,B,(lenA + lenB)/2 + 1)
		else:
			return self.getKth(A,B,(lenA + lenB)/2) + self.getKth(A,B,(lenA + lenB)/2 + 1)*0.5


a = Solution()
res = a.findMedianSortedArrays(A,B)
print(res)			