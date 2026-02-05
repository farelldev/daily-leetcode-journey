# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next

        fst = head
        snd = s
        curr = snd.next
        while curr:
            nxt = curr.next
            curr.next = snd
            snd = curr
            curr = nxt

        while snd != fst:
            nxt = fst.next
            prev = snd.next

            fst.next = snd
            fst = nxt
            if snd == fst: break
            snd.next = fst
            snd = prev

        fst.next = None