class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        for i in range(len(s)):
            if s[i] == "M":
                number += 1000
                if i > 0 and s[i-1] == "C":
                    number -= 200
            elif s[i] == "D":
                number += 500
                if i > 0 and s[i-1] == "C":
                    number -= 200
            elif s[i] == "C":
                number += 100
                if i > 0 and s[i-1] == "X":
                    number -= 20
            elif s[i] == "L":
                number += 50
                if i > 0 and s[i-1] == "X":
                    number -= 20
            elif s[i] == "X":
                number += 10
                if i > 0 and s[i-1] == "I":
                    number -= 2
            elif s[i] == "V":
                number += 5
                if i > 0 and s[i-1] == "I":
                    number -= 2
            else:             #s[i] == "I":
                number += 1
                
        return number
                
                
