class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rsize, csize=len(image), len(image[0])
        visited=[[0]*csize for i in range(rsize)]
        def run(r, c, oldColor):
            if not 0<=r<rsize or not 0<=c<csize or visited[r][c]==1 or image[r][c]!=oldColor:
                return
            image[r][c]=newColor
            visited[r][c]=1
            run(r-1, c, oldColor)
            run(r, c-1, oldColor)
            run(r+1, c, oldColor)
            run(r, c+1, oldColor)
        run(sr, sc, image[sr][sc])
        return image
