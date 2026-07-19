# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1

        dummy_head = ListNode(0) 
        node = dummy_head
        pt1, pt2 = list1, list2

        while pt1 and pt2:
            if pt1.val < pt2.val:
                node.next = pt1
                pt1 = pt1.next
            else:
                node.next = pt2
                pt2 = pt2.next
            node = node.next
        if pt1:
            node.next = pt1
        if pt2:
            node.next = pt2
        
        return dummy_head.next

                    