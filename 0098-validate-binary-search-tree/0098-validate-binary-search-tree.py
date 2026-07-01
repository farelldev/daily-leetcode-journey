# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        traversal = []

        def inorder(node):
            if not node: return

            inorder(node.left)
            traversal.append(node.val)
            inorder(node.right)

        inorder(root)

        res = traversal == sorted(traversal) and len(traversal) == len(set(traversal))
        return res