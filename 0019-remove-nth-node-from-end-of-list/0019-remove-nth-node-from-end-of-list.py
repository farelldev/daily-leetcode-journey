# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, N = head, 0

        while curr:
            curr = curr.next
            N += 1

        remove = N - n
        curr, prev = head, None
        
        for _ in range(remove):
            prev = curr
            curr = curr.next

        nxt = curr.next
        if prev:
            prev.next = nxt
        curr.next = None
        
        if prev: return head
        else: return nxt