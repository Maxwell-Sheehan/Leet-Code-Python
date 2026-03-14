# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None: # if both are empty, they're symetrical
            return True

        elif p is None or q is None: # if one is empty, they're not symetrical
            return False

        if p.val == q.val: #if the root value is the same, check if tthe children are the same, if not false
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        return False