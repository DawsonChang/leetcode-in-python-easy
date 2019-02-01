class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = n
        listPut = []
        listPut.append(n)
        while(1):
                prod = 0
                S = str(m)
                L = list(S)
                #print(L)
                for item in L:
                    prod += int(item)**2
                if prod == 1:
                    return True
                if prod in listPut:
                    return False
                listPut.append(prod)
                m = prod
