class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentList=sentence.split()
        dictSet=set(dict)
        dictSetLength={len(d) for d in dictSet}
        dictSetLength=list(dictSetLength)
        dictSetLength.sort()
        for i in range(len(sentList)):
            for l in dictSetLength:
                if sentList[i][:l] in dictSet:
                    sentList[i]=sentList[i][:l]
                    break
        return ' '.join(sentList)
