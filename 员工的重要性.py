em = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
id = 1

class Solution:
	def __init__(self):
		self.ids = {}
		self.sum = 0
	def impor(self,em,id):
		for i in em:
			self.ids[i[0]] = (i[1],i[2])
		self.dfs(self.ids[id][0],self.ids[id][1])
		return self.sum

	def dfs(self,val,ems):
		self.sum += val
		for i in ems:
			self.dfs(self.ids[i][0],self.ids[i][1])

a = Solution()
print(a.impor(em,id))








