# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        res = ListNode()
        prev = res

        curr = head
        prev.next = curr
        nxt = curr.next

        while nxt:
            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt

            prev = curr
            curr = curr.next
            nxt = curr.next if curr else None

        return res.next