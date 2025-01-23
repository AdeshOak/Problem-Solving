class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        n = len(s)
        l=0
        cnt = 0
        for r in range(n):
            while s[r] in s[l:r]:
                l+=1
            cnt = (r-l)+1
            longest = max(longest,cnt)

        return longest


# Time: O(n) Outer loop executes n times and inner while loop mostly lesser than that but can be executed at most n times
# Space: O(1) Constant space for variables
