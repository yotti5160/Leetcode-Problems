class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        book={()}
        for i in range(len(nums)):
            tmp=set()
            for b in book:
                if not b:
                    tmp.add((nums[i],))
                elif nums[i]>=b[-1]:
                    tmp.add(b+(nums[i],))
            book|=tmp
        return [list(b) for b in book if len(b)>1]  
