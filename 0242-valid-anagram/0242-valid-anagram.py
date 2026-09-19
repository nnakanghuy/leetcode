#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for idx in set(s):
            if s.count(idx) != t.count(idx):
                return False
        return True