# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 迭代法
        if not head:
            return head
        oldnode = head
        newnode = None

        while (oldnode):
            oldnextnode = oldnode.next

            oldnode.next = newnode

            newnode = oldnode

            oldnode = oldnextnode

        return newnode
            


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
s = Solution()
print(s.reverseList(n1))





