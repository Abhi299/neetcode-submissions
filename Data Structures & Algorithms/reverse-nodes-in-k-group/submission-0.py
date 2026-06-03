# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, next = None, head, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(-1)
        prev_tail = sentinel
        l = r = head

        while True:
            t = k - 1
            while r and t:
                r, t = r.next, t - 1
            if not r: break

            temp = r.next
            r.next = None
            r = temp
            new_head = self.reverseList(l)

            prev_tail.next = new_head
            prev_tail = l
            l = r

        prev_tail.next = l
        return sentinel.next