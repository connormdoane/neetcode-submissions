# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not q or not p:
            return None
        
        res = root
        while res:
            if q.val < res.val and p.val < res.val:
                res = res.left
            elif q.val > res.val and p.val > res.val:
                res = res.right
            else:
                return res