class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        index = 0

        for x in s:
            if index < len(t) and x == t[index]:
                index += 1

        return len(t) - index