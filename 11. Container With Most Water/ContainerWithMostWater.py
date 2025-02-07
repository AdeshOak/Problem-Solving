class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        waterHeld = 0
        leftptr = 0
        rightptr = len(height) - 1

        while leftptr <= rightptr:
            reqheight = min(height[leftptr], height[rightptr])
            width = rightptr - leftptr
            area = reqheight * width

            waterHeld = max(waterHeld,area)

            if height[leftptr] > height[rightptr]:
                rightptr -= 1
            else:
                leftptr += 1
        return waterHeld
        

# T: O(n)
# S: O(1)
