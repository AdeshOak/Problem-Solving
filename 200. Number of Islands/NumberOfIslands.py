class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid) #<- rows
        n = len(grid[0]) #<- cols
        countIslands = 0

        if not grid:
            return 


        def dfsStack(i,j):
            stk = [(i,j)]
            while stk:
                row, col = stk.pop()

                while 0<= row < m and 0<=col <n and grid[row][col] == '1':
                    grid[row][col] = '0'
                    stk.append((row-1,col))
                    stk.append((row+1,col))
                    stk.append((row,col-1))
                    stk.append((row,col+1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    countIslands += 1
                    dfsStack(i,j)
        
        return countIslands

T: O(mxn)
S: O(mxn)
