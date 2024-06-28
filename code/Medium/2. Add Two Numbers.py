# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1cur = l1
        l2cur = l2
        up = 0
        re = ListNode()
        cur = re
        while True: 
            if l1cur == None and l2cur == None:
                if up == 1:
                    cur.next = ListNode(1)
                break
            
            if l1cur == None:
                Sum = l2cur.val + up
                l2cur = l2cur.next
            elif l2cur == None:
                Sum = l1cur.val + up
                l1cur = l1cur.next
            else:
                Sum = l1cur.val + l2cur.val + up
                l1cur,l2cur = l1cur.next, l2cur.next
            newnode = ListNode(Sum%10)
            up = Sum // 10
            cur.next = newnode
            cur = cur.next
            
        return re.next
