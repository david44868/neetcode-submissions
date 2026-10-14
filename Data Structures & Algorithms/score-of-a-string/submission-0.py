class Solution:
    def scoreOfString(self, s: str) -> int:
        
        index = 0
        val = 0

        while index < len(s) - 1:
            val += abs(ord(s[index]) - ord(s[index + 1]))
            index += 1
        
        return val
