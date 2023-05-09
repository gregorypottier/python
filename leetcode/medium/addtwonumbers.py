# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carry: # runs when l1, l2, or carry are not None, 0s, or empty iterables
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10 # if we exceed ten, we must add one more to next combination of values
            curr.next = ListNode(total % 10) # new ListNode object becomes curr.next 
            curr = curr.next # move curr to point to its next ListNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
