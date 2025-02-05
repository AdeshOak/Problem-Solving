from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""

        tFreq = defaultdict(int)
        for char in t:
            tFreq[char] += 1

        sWindowFreq = defaultdict(int)
        l = 0
        matched = 0
        minLen = float('inf')
        minWindow = ""

        for r in range(len(s)):
            charR = s[r]

            if charR in tFreq:
                sWindowFreq[charR] += 1

                if sWindowFreq[charR] == tFreq[charR]:
                    matched += 1

            
            while matched == len(tFreq):
                if r-l+1 < minLen:
                    minLen = r-l+1
                    minWindow = s[l:r+1]

                charL = s[l]
                if charL in sWindowFreq:
                    sWindowFreq[charL] -= 1
                    if sWindowFreq[charL] < tFreq[charL]:
                        matched -= 1

                l += 1

        return minWindow


# Time Complexity: O(n + m), where n is the length of t and m is the length of s.
# Space Complexity: O(k + m), where k is the number of unique characters in t and m is the length of s.
