class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def run(person):
            if visited[person]:
                return
            visited[person]=1
            for p in flist[person]:
                run(p)
            return
        l=len(M)
        flist=[[] for i in range(l)]
        for i in range(l):
            for j in range(l):
                if M[i][j]:
                    flist[i].append(j)
        self.ret=0
        visited=[0]*l
        for i in range(l):
            if visited[i]==0:
                self.ret+=1
                run(i)
        return self.ret
