# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)
        curr = head
        cnt = 1

        while curr:
            if cnt == 1:
                hc = curr
                cnt += 1
                curr = curr.next

            elif cnt == k:
                swap = hc
                ns = swap.next

                while swap != curr:
                    ps = swap
                    swap = ns
                    ns = swap.next
                    
                    swap.next = ps

                prev.next = curr
                hc.next = ns

                curr = hc.next
                cnt = 1

                prev = hc

            else:
                curr = curr.next
                cnt += 1

        return dummy.next