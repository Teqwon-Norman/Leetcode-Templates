# Tree class
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root: TreeNode) -> None:
    if not root:
        return
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)
