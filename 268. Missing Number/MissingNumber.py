class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sumA=0
        sumT = (n* (n+1)) / 2
        for i in range(n):
            sumA += nums[i]

        return (sumT - sumA)

  #Time - O(n)
  #Space - O(1)
