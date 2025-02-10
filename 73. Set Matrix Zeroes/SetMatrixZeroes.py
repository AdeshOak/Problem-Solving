from collections import deque
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        q = deque()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i,j))

        while q:
            
            i,j = q.popleft()
            # Set entire row to zero
            for k in range(n):
                matrix[i][k] = 0

            # Set entire column to zero
            for k in range(m):
                matrix[k][j] = 0
