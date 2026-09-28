# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fst = head
        slw = head
        while fst is not None and fst.next is not None:
            fst = fst.next.next
            slw = slw.next
            if fst == slw:
                return True
        return False