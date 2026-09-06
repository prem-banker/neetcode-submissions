# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ans = head

        while(list1 or list2):
            if list1:
              val1 = list1.val
            else:
                val1 = 9000

            if list2:
                val2 = list2.val
            else:
                val2 = 9000

            if val1 < val2:
                ans.next = ListNode(val1)
                list1 = list1.next
            elif val2 < val1:
                ans.next =  ListNode(val2)
                list2 = list2.next
            else:
                ans.next =  ListNode(val1)
                ans = ans.next
                ans.next =  ListNode(val2)
                list1 = list1.next
                list2 = list2.next

            
            ans = ans.next
        return head.next