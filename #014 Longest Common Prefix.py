class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        i = 0
        while i < len(strs[0]):
            s = strs[0][:i+1]
            for item in strs:
                if item[:i+1] != s:
                    return item[:i]
            i += 1
                
        return strs[0]
