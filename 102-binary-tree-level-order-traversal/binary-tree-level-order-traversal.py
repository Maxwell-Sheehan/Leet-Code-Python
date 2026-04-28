# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        queue = deque([root])
        res = []

        while len(queue) > 0:
            new_level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                new_level.append(node.val)

                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
                
            res.append(new_level)
        
        return res