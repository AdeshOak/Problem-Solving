# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1ptr = list1
        l2ptr = list2
        mergedHead = ListNode()
        current = mergedHead

        while l1ptr and l2ptr:
            if l1ptr.val < l2ptr.val:
                current.next = l1ptr
                l1ptr = l1ptr.next 
            else:
                current.next = l2ptr
                l2ptr = l2ptr.next
            current = current.next

        if l1ptr:
            current.next = l1ptr
        if l2ptr:
            current.next = l2ptr

        return mergedHead.next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1ptr = list1
        l2ptr = list2
        mergedHead = ListNode()
        current = mergedHead

        while l1ptr and l2ptr:
            if l1ptr.val < l2ptr.val:
                current.next = l1ptr
                l1ptr = l1ptr.next 
            else:
                current.next = l2ptr
                l2ptr = l2ptr.next
            current = current.next

        if l1ptr:
            current.next = l1ptr
        if l2ptr:
            current.next = l2ptr

        return mergedHead.next


# Time : O(m+n) where m is length of list1 and n is length of list2 since we traverse both 
# Space : O(1) constant space used
