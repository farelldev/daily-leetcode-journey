# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxx):
            if not node: return 0

            cnt = 1 if node.val >= maxx else 0
            maxx = max(maxx, node.val)
            cnt += dfs(node.left, maxx)
            cnt += dfs(node.right, maxx)
            
            return cnt

        return dfs(root, root.val)
            