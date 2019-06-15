l = [1,2,3,4,5]

class Solution:
	def permute(self,num):
		Solution.lists = []
		val = []
		Solution.n = len(num)
		self.dfs(num,val)
		return Solution.lists

	def dfs(self,num,val):
		if len(val) == Solution.n:
			Solution.lists.append(val)
			val = []
		for i,j in enumerate(num):
			self.dfs(num[:i]+num[i+1:],val+[j])


a = Solution()
print(a.permute(l))






