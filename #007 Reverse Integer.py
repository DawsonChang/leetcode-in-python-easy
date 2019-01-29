class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        is_neg = 0
        if s[0] == "-":
            is_neg = 1
        if is_neg == 0:
            s = s[::-1]
            if (int(s) > 2**31-1):
                return 0
            return int(s)
        else:
            s = s[:0:-1]
            if (0-int(s) < 0-2**31):
                return 0
            return 0-int(s)
