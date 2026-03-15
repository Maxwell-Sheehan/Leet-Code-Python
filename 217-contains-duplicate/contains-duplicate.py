class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen: # if num is in the set already, its not unique
                return True
            seen.add(num) # add the num to the seen set

        return False # if these checks fail, then it's false