class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        curr = head
        while curr and curr.next != None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

  #Time Complexity : O(n)
  #Space Complexity : O(1)
