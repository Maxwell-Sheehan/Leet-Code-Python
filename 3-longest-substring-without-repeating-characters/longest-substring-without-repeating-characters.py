class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0

        counter: dict[str,int] = defaultdict(int)
        for r in range(len(s)):
            counter[s[r]] +=1 # for each character at index r, we add it to our coutner dict
            while counter[s[r]]  > 1:  # if the character added appears more then once
                                    # we have aduplicate and need to remove it
                counter[s[left]] -=1 # close left window to remove duplicate
                left += 1
            longest = max(longest, r - left + 1)
        return longest