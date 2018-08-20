class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def check(i,j,d):
            if (0<=i-1<m and 0<=j<n and ret[i-1][j]==d) or \
            (0<=i<m and 0<=j-1<n and ret[i][j-1]==d) or \
            (0<=i+1<m and 0<=j<n and ret[i+1][j]==d) or \
            (0<=i<m and 0<=j+1<n and ret[i][j+1]==d):
                ret[i][j]=d+1
                self.count+=1
                return
            
        m,n=len(matrix), len(matrix[0])
        ret=[[None]*n for _ in range(m)]
        self.count=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    ret[i][j]=0
                    self.count+=1
        d=0
        while self.count<m*n:
            for i in range(m):
                for j in range(n):
                    if ret[i][j]==None:
                        check(i,j,d)
            d+=1
        return ret
