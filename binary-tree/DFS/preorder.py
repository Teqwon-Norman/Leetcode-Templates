# Tree class
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root: TreeNode) -> None:
    if not root:
        return
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)
