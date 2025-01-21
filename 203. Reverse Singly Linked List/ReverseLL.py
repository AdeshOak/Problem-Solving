class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        previousNode = None 
        currentNode = head

        while currentNode:
            tempNode = currentNode.next
            currentNode.next = previousNode #Reversal
            #Shift pointers
            previousNode = currentNode
            currentNode = tempNode
        
        return previousNode

  #Time complexity : O(n) Since we need to traverse the entire LinkedList with size n once to reverse it 
  #Space complexity: O(1) using constant space for the required variables
