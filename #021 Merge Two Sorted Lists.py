# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

        
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            result = cur = ListNode(0)
            '''if l1.val < l2.val:
                cur = l1
                l1 = l1.next
            else:
                cur = l2
                l2 = l2.next
            cur = cur.next'''
            while l1 != None and l2 != None:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return result.next
                
                
                
                
                
                
                
        
