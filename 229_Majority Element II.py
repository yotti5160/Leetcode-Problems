class Solution:
    #O(N) time, O(1) space
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s1, s2=None, None
        c1, c2=0, 0
        for n in nums:
            if n==s1:
                c1+=1
            elif n==s2:
                c2+=1
            elif c1==0:
                s1=n
                c1=1
            elif c2==0:
                s2=n
                c2=1
            else:
                c1-=1
                c2-=1
        return [n for n in (s1, s2) if nums.count(n)>len(nums)//3]
