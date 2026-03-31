class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = len(s) - 1

        while s[last_word] == " ":
            last_word -=1

        start = last_word

        while start >= 0 and s[start] != " ":
            start -= 1

        return last_word - start 

        
