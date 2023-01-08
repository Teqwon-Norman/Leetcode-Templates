from collections import deque

# Tree class
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelorder(root: TreeNode) -> None:
    q = deque([root])

    while q:
        size = len(q)

        for _ in range(size):
            curr = q.popleft()

            if not curr:
                continue

            q.append(curr.left)
            q.append(curr.right)
    return 