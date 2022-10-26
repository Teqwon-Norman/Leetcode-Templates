# Tree class
import collections


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def levelorder(root: TreeNode) -> None:
    if not root:
        return
    q = collections.deque([root])

    while q:
        size = len(q)
        for i in range(size):
            curr = q.popleft()
            print(str(curr.val), end=" ")
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
             