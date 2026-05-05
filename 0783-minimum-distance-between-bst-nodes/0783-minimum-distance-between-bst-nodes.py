# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        order = []

        def traverse(node):
            if not node: return

            traverse(node.left)
            order.append(node.val)
            traverse(node.right)

        traverse(root)
        res = order[1] - order[0]

        for i in range(len(order) - 1):
            cur = order[i+1] - order[i]
            res = min(cur,res)

        return res