class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = []
        for item in s:
            if item == ')' or item == ']' or item == '}':
                if len(L) == 0:
                    return False
                '''if L[-1] != '(' and L[-1] != '[' and L[-1] != '{':
                    return False'''
            if item == '(' or item =='[' or item == '{':
                L.append(item)
            if item == ')':
                if L[-1] == '(':
                    del L[-1]
                else:
                    return False
            if item == ']' :
                if L[-1] == '[':
                    del L[-1]
                else:
                    return False
            if item == '}':
                if L[-1] == '{':
                    del L[-1]
                else:
                    return False
        if len(L) == 0:
            return True
        else:
            return False
                
            
        
