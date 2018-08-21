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
        nowOn=['0000']
        output=1
        while nowOn:
            nextOn=[]
            for n in nowOn:
                for i in range(4):
                    num=int(n[i])
                    tmp=n[:i]+str((num+1)%10)+n[i+1:]
                    if tmp==target:
                        return output
                    elif tmp not in visited:
                        nextOn.append(tmp)
                        visited.add(tmp)
                    tmp=n[:i]+str((num-1)%10)+n[i+1:]
                    if tmp==target:
                        return output
                    elif tmp not in visited:
                        nextOn.append(tmp)
                        visited.add(tmp)
            nowOn=nextOn
            output+=1
        return -1
