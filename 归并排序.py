class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: ListNode) -> ListNode:
    # 递归终止条件：链表为空或只有一个节点
    if not head or not head.next:
        return head
    
    # 使用快慢指针找到链表中点
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # 将链表拆分成两个子链表
    mid = slow.next
    slow.next = None
    
    # 对两个子链表分别进行归并排序
    left = sortList(head)
    right = sortList(mid)
    
    # 合并两个有序子链表
    dummy = ListNode(0)
    curr = dummy
    while left and right:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    
    curr.next = left or right
    
    return dummy.next
"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 
例子：head = [4,2,1,3]
输出：[1,2,3,4]

使用方法：

假设链表为 head = ListNode(4, ListNode(2, ListNode(1, ListNode(3)))) ，则调用 sortList(head) 即可得到排好序的链表。

注意：代码中的 ListNode 类定义了链表节点的数据结构，它包含一个 val 属性表示节点的值，以及一个 next 属性表示下一个节点的指针。在调用 sortList 函数时，需要传入链表的头节点 head。
"""