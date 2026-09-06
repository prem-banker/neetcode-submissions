# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while(True):
 
            if slow:
                slow = slow.next
        
            if fast and fast.next:
                fast = fast.next.next

            if fast == slow:
                return True

            if fast == None or slow == None:
                return False
        return False

