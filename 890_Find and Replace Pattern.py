class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def pat(s1,s2):
            return len(set(s1))==len(set(s2))==len(set(zip(s1,s2)))
        r=[]
        for w in words:
            if pat(w,pattern):
                r.append(w)
        return r
