class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        prev_step = 3
        prev_step2 = 2
        curr = 0

        for i in range(3, n):
            curr = prev_step + prev_step2
            prev_step2 = prev_step
            prev_step = curr

        
        return curr