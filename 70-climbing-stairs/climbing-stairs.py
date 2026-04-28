class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        curr = 0
        prev_step = 3
        prev_step2 = 2

        for i in range(3, n):

            curr = prev_step + prev_step2
            prev_step2 = prev_step
            prev_step = curr

        return curr
