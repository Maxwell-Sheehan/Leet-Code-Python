class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            m = (left + right) //2

            if m*m == x:
                return m

            elif m*m < x:
                left = m + 1
            
            elif m*m > x:
                right = m -1

        return m-1 if m*m > x else m
        