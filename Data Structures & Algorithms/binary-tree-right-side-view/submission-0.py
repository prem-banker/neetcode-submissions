# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = [root.val]
        curr = deque([root])

        while (True):
            for i in range(len(curr)):
                popped = curr.popleft()
                if popped.right:
                    curr.append(popped.right)
                if popped.left:
                    curr.append(popped.left)

            if len(curr) > 0:
                ans.append(curr[0].val)
            else:
                return ans