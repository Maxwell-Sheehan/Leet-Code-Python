class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        roman = {
            "I" : 1, "V" : 5,
            "X" : 10, "L" : 50,
            "C" : 100, "D" : 500,
            "M" : 1000
        }

        for i in range(len(s) - 1):
            if roman[s[i]] >= roman[s[i+1]]:
                total += roman[s[i]]
            
            elif roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]

    
        total += roman[s[-1]]
        return total

        #M C M X C I V

        #1000
        # 900
        # 1900
        #

                #if val.right > val. left
                # add value to total
                # if left > right

