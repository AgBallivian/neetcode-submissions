class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for letter in s:
            if t.count(letter) != s.count(letter):
                return False
        return True