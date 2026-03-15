from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = [] #need to store result array for node levels
        queue = deque([root]) #use a queue to control order traversal, first in first out
        
        while len(queue) > 0: #if the queue is not empty loop
            n = len(queue)  # set n to length of queue
            new_level = [] #create an empty subarray for the new level

            for _ in range(n): # for each node we will add its children to teh queue
                node = queue.popleft() #add current levels children to queue
                new_level.append(node.val) #append teh value to new level array

                for child in [node.left, node.right]: 
                    if child is not None:
                        queue.append(child)
            res.append(new_level) #appen to result the levels results for finished prodcut
        return res