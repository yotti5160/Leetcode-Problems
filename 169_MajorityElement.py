class Solution:
    #O(1) time
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        stack=None
        for n in nums:
            if count==0:
                stack=n
                count=1
            elif stack==n:
                count+=1
            else:
                count-=1
        return stack
