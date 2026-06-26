# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = []

        def traverse(node):
            if not node: return
            traverse(node.left)
            
            if len(traversal) == k: return
            traversal.append(node.val)

            if len(traversal) == k: return
            traverse(node.right)

        traverse(root)
        res = traversal.pop() if traversal else None
        return res