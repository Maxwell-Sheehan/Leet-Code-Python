class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")":"(", "]":"[", "}":"{"}

        for char in s:
            if char in map.values():
                stack.append(char)
            if char in map.keys():
                if not stack or stack.pop() != map[char]:
                    return False
        return not stack