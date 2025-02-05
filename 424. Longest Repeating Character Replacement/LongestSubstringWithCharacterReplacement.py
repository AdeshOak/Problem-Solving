from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        '''

        - initialize pointers for window limites
        - Maintain a frequency dictionary to keep a count of frequencies of the characters
          encountered till now 
        - loop rightptr till end:
            * increment frequency of character at rightPtr by 1 
            * update windowsize (right - left + 1)
            * retrieve most popular char frequency in current window 
            # check condition -> if (total size of window i.e. total chars in window) - frequency of most popular character > k <- This suggests more than k replacements required
                => reduce frequency of character at leftptr by 1
                => Increment leftptr by 1 (shrink window)
                => recalculate window size 

            *update result variable to be max of itself or currentWindowlength 


        '''

        res = 0
        leftPtr = 0
        curLen = 0
        frequencies = defaultdict(int)
        for rightPtr in range(len(s)):
            frequencies[s[rightPtr]] += 1
            curLen = rightPtr - leftPtr + 1
            mostPopChar = max(frequencies.values())

            if curLen - mostPopChar > k:
                frequencies[s[leftPtr]] -= 1
                leftPtr += 1
                curLen = rightPtr - leftPtr + 1

            res = max(res,curLen)
        
        return res
