from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False 
        sSet = defaultdict(int)
        tSet = defaultdict(int)

        for i in range(len(s)):
            sSet[s[i]] += 1
            tSet[t[i]] += 1
        
        if sSet == tSet: 
            return True 
        return False

#T: O(n)
#S: O(1)
