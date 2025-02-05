class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curSum = 0
        avg = 0
        for i in range(k):
             curSum += nums[i]
        maxAvg = curSum/ float(k)

        for i in range(k,len(nums)):
            curSum+= nums[i] - nums[i-k]

            avg = curSum/ float(k)
            maxAvg = max(maxAvg,avg)
        return maxAvg

T: O(n)
