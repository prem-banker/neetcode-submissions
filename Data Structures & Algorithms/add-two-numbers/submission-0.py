# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ans = head
        carry = 0
        while(l1 or l2):
            val = 0
            if l1:
                val+=l1.val
                l1 = l1.next
            if l2:
                val+=l2.val
                l2 = l2.next
            
            if carry:
                val+=1
            if val >= 10:
                carry = 1
                ans.next = ListNode(val-10)

            else:
                ans.next = ListNode(val)
                carry = 0
                
            ans = ans.next
    
        if carry == 1:
            ans.next = ListNode(1)
        return head.next