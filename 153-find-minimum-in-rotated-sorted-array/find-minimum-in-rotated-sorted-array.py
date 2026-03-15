class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        boundary_index = -1 #default value as we compare againt

        while left <= right:
            mid = (left + right) //2 #classic binary search, whiile left and right don't touch, set midpoint

            if nums[mid] <= nums[-1]: #if the mid value, is smaller then the last value, 
                boundary_index = mid # the min(boundary_index) is updated to our mid
                right = mid - 1 # we then lower the right edge, till we find the true mid
            else:
                left = mid + 1 # if the mid > num, left becomes one position to the right of mid

        return nums[boundary_index]

