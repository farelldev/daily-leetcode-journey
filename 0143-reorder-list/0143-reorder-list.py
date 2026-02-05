# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # get first & second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        first = head
        second = slow
        curr = second.next

        while curr:
            nxt = curr.next
            curr.next = second
            second = curr
            curr = nxt

        # reorder the list
        while second != first:
            first_next = first.next
            second_next = second.next

            first.next = second
            first = first_next

            if second == first:
                break

            second.next = first
            second = second_next

        # cut the edge
        first.next = None