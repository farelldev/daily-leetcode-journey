# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = collections.deque()
        q.append(root)
        
        if not root: return res

        while q:
            qlen = len(q)

            for i in range(qlen):
                node = q.popleft()

                if node:
                    if not node.left and not node.right:
                        return res + 1

                    q.append(node.left)
                    q.append(node.right)
            
            res += 1