class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        ret, balance=0, 0
        for s in S:
            if s=='(':
                balance+=1
            else:
                balance-=1
            if balance<0:
                balance+=1
                ret+=1
        return ret+balance
