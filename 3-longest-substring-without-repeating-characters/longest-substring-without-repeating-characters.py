class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0

        counter: dict[str,int] = defaultdict(int)

        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 1:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, r - left + 1)
        return longest
        