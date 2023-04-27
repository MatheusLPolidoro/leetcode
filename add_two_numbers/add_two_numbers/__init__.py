class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head


def toList(head):
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst


class Solution(object):
    """
    >>> Solution().addTwoNumbers(createLinkedList([2, 4, 3]), createLinkedList([5, 6, 4]))
    [7, 0, 8]
    >>> Solution().addTwoNumbers(createLinkedList([0]), createLinkedList([0]))
    [0]
    >>> Solution().addTwoNumbers(createLinkedList([9,9,9,9,9,9,9]), createLinkedList([9,9,9,9]))
    [8, 9, 9, 9, 0, 0, 0, 1]
    """

    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = n = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            n.next = n = ListNode(val)
        return toList(res.next)
