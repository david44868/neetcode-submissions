class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(list(s).sort)
        print(list(t).sort)
        return True if sorted(list(s)) == sorted(list(t)) else False
