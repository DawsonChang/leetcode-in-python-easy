class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        D = dict(zip(s[::-1],t[::-1]))
        #print(D)
        if len(D) != len(set(D.values())):
            return False
        j = 0
        for i in s:
            if D[i] != t[j]:
                return False
            j += 1
        return True
        
