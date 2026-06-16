# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, mn, mx):
            if not node:
                return True
            left = dfs(node.left, mn, node.val) if node.left else True
            right = dfs(node.right, node.val, mx) if node.right else True
            return node.val > mn and node.val < mx and left and right

        return dfs(root, -1001, 1001)