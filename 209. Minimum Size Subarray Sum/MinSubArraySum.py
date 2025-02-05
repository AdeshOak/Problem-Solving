class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        res = float('inf')
        curSum = 0

        for j in range(len(nums)):
            curSum += nums[j]


            while curSum >= target:
                res = min(res, j - i + 1)
                curSum -= nums[i]
                i += 1

        return res if res != float('inf') else 0
