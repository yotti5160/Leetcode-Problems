class Solution:
    #O(N+M) time and space, where M=len(times), 
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        spread=collections.defaultdict(list)
        for (u, v, w) in times:
            spread[u-1].append((v-1,w))
        distance=[float('inf')]*N
        distance[K-1]=0
        NotVisited=set([i for i in range(N)])
        while NotVisited:
            nowNode=None
            for node in NotVisited:
                if nowNode==None or distance[node]<distance[nowNode]:
                    nowNode=node
            if distance[nowNode]==float('inf'):
                return -1
            NotVisited.remove(nowNode)
            for (nextNode,d) in spread[nowNode]:
                tmp=distance[nowNode]+d
                if tmp<distance[nextNode]:
                    distance[nextNode]=tmp
        return max(distance) 
