# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def countGood(maxVal, root):
            if not root:
                return 0

            if root.val >= maxVal:
                maxVal = max(maxVal, root.val)
                return 1 + countGood(maxVal, root.left) + countGood(maxVal, root.right) 
            else:
                return countGood(maxVal, root.left) + countGood(maxVal, root.right)

        return countGood(-100000, root)