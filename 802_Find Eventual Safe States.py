class Solution:
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        def dfs(start):
            if visited[start]!=0:
                return visited[start]==2
            visited[start]=1
            for j in graph[start]:
                if not dfs(j):
                    return False
            visited[start]=2
            return True
        l=len(graph)
        visited=[0]*l
        ret=[]
        for i in range(l):
            if dfs(i):
                ret.append(i)
        return ret      
