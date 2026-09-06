# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True


        leftdepth = 0 if not root.left else 1 + self.depth(root.left)
        rightdepth = 0 if not root.right else 1 + self.depth(root.right)  
        return abs(leftdepth - rightdepth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))