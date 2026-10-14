class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) > len(t):
            return False

        index = 0
        for x in t:
            if index < len(s) and x == s[index]:
                index += 1
        
        return True if len(s) == index else False