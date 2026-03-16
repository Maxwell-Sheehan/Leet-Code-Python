class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = sorted(nums1 + nums2)
        length = len(array)

        #check if even or odd for median
        if length % 2 == 0:
            return (array[length // 2 - 1] + array[length // 2]) /2
        else: #it's even or odd so only two cases
            # if odd return the middle
            return array[length // 2]
