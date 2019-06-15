'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
'''
m = 0
def tree(root):
	if not root:
		return 0
	self.maxlen(root,root.val)
	return self.m

	def maxlen(self,root,val):
		if not root:
			return 0
		left = maxlen(root.left,root.val)
		right = maxlen(root.right,root.val)
		self.m = max(left+right,self.m)
		if root.val 








