class Solution:
    def coinChange(self, coins, amount):
        
        def dfs(amount, nowCount, startIndex):
            if nowCount+math.ceil(amount/coins[startIndex])>=self.ret:
                return
            if amount%coins[startIndex]==0:
                self.ret=min(self.ret, nowCount+amount//coins[startIndex])
                return
            if startIndex==l-1:
                return
            for i in range(amount//coins[startIndex], -1, -1):
                dfs(amount-i*coins[startIndex], nowCount+i, startIndex+1)
            return
                
        self.ret=amount+1
        l=len(coins)
        coins.sort(reverse=True)
        dfs(amount, 0, 0)
        return self.ret if self.ret<(amount+1) else -1
