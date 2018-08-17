class Solution:
    #O(N) time, O(1) space
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=[0]*len(nums)
        p=1
        for i in range(len(nums)):
            r[i]=p
            p*=nums[i]
        p=1
        for i in range(len(nums)-1,-1,-1):
            r[i]*=p
            p*=nums[i]
        return r
