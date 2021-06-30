# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        tail = dummyNode
        while True :
            if l1 is None :
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break
                
            if l1.val <= l2.val :
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
 
            tail = tail.next
 
    
        return dummyNode.next