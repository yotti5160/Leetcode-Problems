class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp=[0]*(target+1)
        dp[0]=1
        for i in range(1,target+1):
            for n in nums:
                if i-n>=0:
                    dp[i]+=dp[i-n]
                else:
                    break
        return dp[target]
