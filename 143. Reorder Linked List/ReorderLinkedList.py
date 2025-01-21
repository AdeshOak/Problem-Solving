class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
      
        slow = head
        fast = slow.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #Reverse the second half
        secondPtr = slow.next
        slow.next = None
        prev = None
        while secondPtr:
            nextNode = secondPtr.next
            secondPtr.next = prev
            prev = secondPtr
            secondPtr = nextNode
        
        #Merge the two lists 
        firstPtr = head
        secondPtr = prev
        while secondPtr:
            firstNext = firstPtr.next
            secondNext = secondPtr.next
            firstPtr.next = secondPtr
            secondPtr.next = firstNext
            firstPtr = firstNext
            secondPtr = secondNext


#Time : O(n) Since we are iterating through the list thrice- once to find mid, once to reverse second half and once to merge 
#Space : O(1) Since we are modifying the list in place
