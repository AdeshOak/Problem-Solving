class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(i,j,pointer):
            if pointer == len(word) : return True 
            if i<0 or i>=m or j<0 or j>=n or board[i][j] != word[pointer]:
                return False
            if pointer == len(word) - 1: return True


            seen.add((i,j))
            neighbors=[(-1,0),(1,0),(0,-1),(0,1)]
            for di,dj in neighbors:
                ni = i+di
                nj = j+dj 
                if (ni,nj) not in seen:
                    if (dfs(ni,nj,pointer+1)):
                        return True
            seen.remove((i,j))
            return False

        m = len(board)
        n = len(board[0])
        seen = set()


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if (dfs(i,j,pointer = 0)):
                        return True

        return False
