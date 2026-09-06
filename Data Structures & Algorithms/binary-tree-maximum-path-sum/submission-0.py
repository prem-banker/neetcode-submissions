# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1000000000
        def findSum(root):
            if not root:
                return -1000000

            if not root.left and not root.right:
                self.ans = max(self.ans, root.val)
                return root.val
            
            left = findSum(root.left)
            right = findSum(root.right)
            self.ans = max(self.ans, root.val, left, right, left + right + root.val, left + root.val, right + root.val)

            return max(root.val, root.val + left, root.val + right )


        findSum(root)
        return self.ans    
            
            
            