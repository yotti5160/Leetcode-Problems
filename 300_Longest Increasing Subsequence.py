class Solution:
    #O(Nlog(N)) time, O(N) space
    def lengthOfLIS(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0
        l=len(A)
        B=[float('inf')]*(l+1)
        B[0]=-float('inf')
        L=1
        for i in range(l):
            if A[i]<B[1]:
                B[1]=A[i]
            else:
                j=bisect.bisect_left(B,A[i])-1 #O(log(N)) time
                B[j+1]=A[i]
                if j+1>L:
                    L+=1
        return L
