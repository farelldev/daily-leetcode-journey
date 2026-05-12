# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def backtrack(root, path):
            path.append(root.val)

            if not root.left and not root.right: 
                path = "->".join(map(str, path))
                res.append(path)
                return

            if root.left: 
                backtrack(root.left, path)
                path.pop()
            if root.right:
                backtrack(root.right, path)
                path.pop()

        backtrack(root, [])
        return res