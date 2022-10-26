# Tree class
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder(root: TreeNode) -> None:
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)

