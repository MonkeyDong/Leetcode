'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''

class Solution:
    def isUnivalTree(self, root):
        if not root:
            return True
        tree = []
        self.fun(root,tree)
        pre = root.val
        for i in tree:
            if i != None and i != pre:
                return False
        return True

    def fun(self,root,tree):
        if root:
            self.fun(root.left,tree)
            tree.append(root.val)
            self.fun(root.right,tree)



