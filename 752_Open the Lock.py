class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if target=='0000':
            return 0
        visited=set(deadends)
        if '0000' in visited:
            return -1
        nowOn={'0000'}
        end={target}
        output=1
        while nowOn:
            nextOn=set()
            for n in nowOn:
                for i in range(4):
                    for k in (-1,1):
                        tmp=n[:i]+str((int(n[i])+k)%10)+n[i+1:]
                        if tmp in end:
                            return output
                        elif tmp not in visited:
                            nextOn.add(tmp)
                            visited.add(tmp)
            nowOn=nextOn
            if len(nowOn)>len(end):
                nowOn, end=end, nowOn
            output+=1
        return -1
