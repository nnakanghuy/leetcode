# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        p = head
        cnt = 0
        while p.next is not None:
            cnt+=1
            p = p.next
        a = head
        tmp = p
        while a.next is not None and a.next.next is not None:
            tmp.next = a.next
            a.next = tmp
            a = a.next.next
            while tmp.next != p:
                tmp = tmp.next
            tmp.next = None
            p = tmp
        

        