class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def hour(input):
            r=[]
            for i in range(12):
                if bin(i).count('1')==input:
                    r.append(str(i)+':')
            return r
        def minute(input):
            r=[]
            for i in range(60):
                if bin(i).count('1')==input:
                    r.append(str(i).zfill(2))
            return r

        result=[]
        for i in range(min(5,num+1)):
            tmpHour=hour(i)
            tmpMin=minute(num-i)
            for h in tmpHour:
                for m in tmpMin:
                    result.append(h+m)
        return result

#test with input num=2
print(Solution.readBinaryWatch(Solution, 2))
