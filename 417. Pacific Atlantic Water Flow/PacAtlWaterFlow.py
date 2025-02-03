class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(heights)  #<- rows
        n = len(heights[0])  #<- cols
        pacSeen = set()
        atlSeen = set()
        pacStk = []
        atlStk = []


        for i in range(n):
            pacSeen.add((0,i))
            pacStk.append((0,i))
            ##print(str((0,i))+ "-" + str(heights[0][i]))

        for i in range(1,m):
            pacSeen.add((i,0))
            pacStk.append((i,0))
            ##print(str((i,0))+ "-" + str(heights[i][0]))

        for j in range(n):
            atlSeen.add((m-1,j))
            atlStk.append((m-1,j))
            ##print(str((m-1,j))+ "-" + str(heights[m-1][j]))

        for j in range(m-1):
            atlSeen.add((j,n-1))
            atlStk.append((j,n-1))
            #print(str((j,n-1))+ "-" + str(heights[j][n-1]))



        def dfsStack(stk, seen):
            dir = [(0,1),(0,-1),(1,0),(-1,0)]
            while stk:
                i,j = stk.pop()
                for roff,coff in dir:
                    r = i+roff
                    c = j+coff
                    if 0 <= r<m and 0 <=c < n and heights[r][c] >= heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        stk.append((r,c))




        
        dfsStack(pacStk,pacSeen)
        #print("Pacific seen set:", pacSeen)
        dfsStack(atlStk,atlSeen)
        #print("Atlantic seen set:", atlSeen)

        return list(pacSeen.intersection(atlSeen))
