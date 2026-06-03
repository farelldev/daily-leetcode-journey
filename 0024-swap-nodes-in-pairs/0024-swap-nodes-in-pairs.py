# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        prev = res

        curr = head
        prev.next = curr
        if not curr: return None
        nxt = curr.next

        while curr and nxt:
            curr.next = nxt.next
            nxt.next = curr
            prev.next = nxt

            prev = curr
            curr = curr.next
            nxt = curr.next if curr else None

        return res.next