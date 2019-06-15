#构建一颗二叉树

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def create(root,lists,i):
    if i<len(lists):
        if lists[i] == '#':
            return None
        else:
            root = TreeNode(lists[i])
            root.left = create(root.left,lists,2*i+1)
            root.right = create(root.right,lists,2*i+2)
            return root
    return None

root=TreeNode(None)
llist=['1','2','3','#','4','5']
root=create(root,llist,0)
print(root.right.left.val)

