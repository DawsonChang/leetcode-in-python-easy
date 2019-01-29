class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        else:
            x = str(x)
            for i in range(int(len(x)/2)):
                if x[i] != x[len(x)-1-i]:
                    return False
        return True
        
