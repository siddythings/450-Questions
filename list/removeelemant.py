# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # [6,2,6,3,4,5,6] ,
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prv = cur = head
        
        while cur:
            if cur.val == val:
                prv.next = cur.next
                cur = cur.next
            else:
                prv = cur
                cur = cur.next
        
        if head and head.val == val:
            head = head.next
            
        return head
