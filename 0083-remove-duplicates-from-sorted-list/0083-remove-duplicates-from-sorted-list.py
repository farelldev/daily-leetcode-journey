# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = curr = head

        while curr:
            curr = curr.next
            while curr and curr.val == prev.val:
                dup = curr
                curr = curr.next
                dup.next = None
            prev.next = curr
            prev = curr
        
        return head