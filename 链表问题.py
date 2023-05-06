"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。请你将两个数相加，并以相同形式返回一个表示和的链表。你可以假设除了数字 0 之外，这两个数都不会以 0 开头
输入: l1 = [2,4,3]，12 = [5,6,4]输出: [7,0,8]
解释: 342 + 465 = 807.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pprint(ListNode):
    l = []
    l.append(ListNode.val)
    if ListNode.next:
        l.extend(pprint(ListNode.next))
    return l
        
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = x + y + carry
        carry = s // 10
        cur.next = ListNode(s % 10)
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry > 0:
        cur.next = ListNode(carry)
    return dummy.next



l1 = ListNode(4, ListNode(5, ListNode(6, ListNode(3))))
l2 = ListNode(7, ListNode(2, ListNode(8)))



# print(pprint(l1))
print(pprint(addTwoNumbers(l1, l2)))