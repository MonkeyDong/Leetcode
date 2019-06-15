# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root):
		self.res = '~'
		
		def dfs(node,arr):
			if node:
				now = chr(node.val + ord('a'))
				arr.append(now)
				if (node.left == None and node.right == None):
					self.res = min(self.res, "".join(reversed(arr)))
				dfs(node.left,arr)
				dfs(node.right,arr)
				arr.pop()
			
		arr = []
		dfs(root,arr)
		return self.res




