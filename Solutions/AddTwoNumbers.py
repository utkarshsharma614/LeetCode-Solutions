# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead=ListNode(0)
        carry=0
        curr=dummyHead
        
        while l1 or l2:
                    if l1:
                        l1_val=l1.val
                    else:
                        l1_val=0
                    if l2:
                        l2_val=l2.val
                    else:
                        l2_val=0
                    
                    sum=l1_val+l2_val+carry
                    curr.next = ListNode(sum % 10)
                    curr=curr.next
                    
                    carry = sum//10
                    
                    if l1:
                        l1=l1.next
                    if l2:
                        l2=l2.next
        
        if carry:
            curr.next=ListNode(carry)
                
        return dummyHead.next
                