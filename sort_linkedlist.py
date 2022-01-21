# 链表排序
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sort_list(self, head):
        h, length, interval = head, 0, 1
        while h:
            h, length = h.next, length + 1
        result = ListNode(0)
        result.next = head
        while interval < length:
            prev, h = result, result.next
            while h:
                h1, i = h, interval
                while i and h:
                    h, i = h.next, i - 1
                if i:
                    break
                h2, i = h, interval
                while i and h:
                    h, i = h.next, i - 1
                c1, c2 = interval, interval - 1
                while c1 and c2:
                    if h1.val < h2.val:
                        prev.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        prev.next, h2, c2 = h2, h2.next, c2 - 1
                    prev = prev.next
                prev.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    prev, c1, c2 = prev.next, c1 - 1, c2 - 1
                prev.next = h
            interval *= 2
        return result.next
