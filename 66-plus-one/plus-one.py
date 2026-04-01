class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        right = len(digits) - 1 

        if digits[right] < 9:
            digits[right] += 1
            return digits

        while right >= 0 and digits[right] == 9:
            digits[right] = 0
            right -= 1
        
        if right >= 0:
            digits[right] +=1
        else:
            digits.insert(0,1)
        
        return digits




        




