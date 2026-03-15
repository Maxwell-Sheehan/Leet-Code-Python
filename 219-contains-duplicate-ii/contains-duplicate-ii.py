class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {} #empty hash map

        for i, num in enumerate(nums): #enumerate the list of #'s
            if num in seen and i - seen[num] <= k: #if the value is seen, and  abs(i - j) <= k.
                return True
            
            else: # otherwise, just add the value to the seen array
                seen[num] = i 
        
        return False #if this stuff aint true, it false