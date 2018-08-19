class Solution:
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        def run(n, color):
            if group[n]!=0:
                return group[n]==color
            group[n]=color
            for i in book[n]:
                if not run(i,-color):
                    return False
            return True

        book=[[] for i in range(N)]
        for d in dislikes:
            book[d[0]-1].append(d[1]-1)
            book[d[1]-1].append(d[0]-1)

        group=[0]*N
        for i in range(N):
            if group[i]==0 and not run(i,1):
                return False
        return True
