# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def dfs(root, m) -> int:
            left = dfs(root.left, max(m, root.val)) if root.left else 0
            right = dfs(root.right, max(m, root.val)) if root.right else 0
            curr = 1 if root.val >= m else 0
            return left + right + curr

        return dfs(root, -101)