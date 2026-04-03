class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        prevStep = 3
        prevStep2 = 2
        curr = 0

        for i in range(3, n):
            curr = prevStep + prevStep2
            prevStep2 = prevStep
            prevStep = curr

        return curr