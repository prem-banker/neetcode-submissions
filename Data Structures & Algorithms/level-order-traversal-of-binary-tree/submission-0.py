# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
                
        if not root:
            return []
        nodes = deque([root])
        path = []
        while (nodes):
            levelpath = []
            for node in nodes:
                levelpath.append(node.val)

            path.append(levelpath)
            
            level = []
            for node in nodes:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            
            nodes= deque(level)
        return path

        