# Tree class
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder(root: TreeNode) -> None:
    if not root:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)

