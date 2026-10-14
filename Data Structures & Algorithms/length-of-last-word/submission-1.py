class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.strip()

        print(s)
        val = 0
        for x in range(len(s) - 1, -1, -1):
            if s[x].isalpha():
                print(s[x])
                val += 1
            else:
                return val
        
        return val