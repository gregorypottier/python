# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode() # initialize head node
        pointer = head # initialize pointer
        while list1 is not None and list2 is not None: # exit loop when one is empty
            if list1.val <= list2.val:
                pointer.next = list1
                list1 = list1.next
            else:
                pointer.next = list2
                list2 = list2.next
            pointer = pointer.next # move pointer
        
        # append remaining values
        if list1 is not None:
            pointer.next = list1
        else:
            pointer.next = list2
        return head.next
