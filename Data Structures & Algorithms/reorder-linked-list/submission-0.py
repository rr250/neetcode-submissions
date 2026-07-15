# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            print('second.val,prev.val', second.val,prev.val if prev is not None else None)

            tmp = second.next
            print('tmp.val',tmp.val if tmp is not None else None)

            second.next = prev
            print('second.next.val', second.next.val if second.next is not None else None)

            prev = second
            print('prev.val', prev.val if prev is not None else None)

            second = tmp
            print('second.val', second.val if second is not None else None)

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2