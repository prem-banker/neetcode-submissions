# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def isValid(node, left, right):
            if not node:
                return True
            return left < node.val < right and isValid(node.left, left, node.val) and isValid(node.right, node.val, right) 

        
        

        return isValid(root, -1000000000000,1000000000000)