class Solution:
    #O(N) time, O(1) space
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r=0
        for i in range(len(grid)):
            r+=grid[i][0]+grid[i][-1]
            for j in range(len(grid[0])):
                if grid[i][j]!=0:
                    r+=2
                if j<len(grid)-1:
                    r+=abs(grid[i][j]-grid[i][j+1])
                if i<len(grid[0])-1:
                    r+=abs(grid[i][j]-grid[i+1][j])
        return r+sum(grid[0])+sum(grid[-1])
