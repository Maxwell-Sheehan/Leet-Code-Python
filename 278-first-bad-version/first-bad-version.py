# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            m = (left + right) // 2
            if isBadVersion(m) == False:
                left = m + 1
                print(m)
            elif isBadVersion(m) == True:
                right = m - 1
                if isBadVersion(m -1) == False:
                    return m
        return m
            
        
