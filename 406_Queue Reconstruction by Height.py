class Solution:
    #O(NlogN) time(sort)
    #First sort the input array by two attributes:
    #(1) height, with reverse order(higher people in front)
    #(2) k, with normal order
    #Then we insert the sorted array into another array with the rule given.
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people=sorted(people, key=lambda p:(-p[0], p[1]))
        r=[]
        for p in people:
            r.insert(p[1], p)
        return r
