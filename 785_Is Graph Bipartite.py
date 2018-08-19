class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def run(n, color):
            if group[n]!=0:
                return group[n]==color
            group[n]=color
            for i in graph[n]:
                if not run(i,-color):
                    return False
            return True
        
        l=len(graph)
        group=[0]*l
        for i in range(l):
            if group[i]==0 and not run(i,1):
                return False
        return True
