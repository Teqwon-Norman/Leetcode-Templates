# Tree class
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root: TreeNode) -> None:
    if not root:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

