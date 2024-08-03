class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            first_node = current.next
            second_node = current.next.next
            
            first_node.next = second_node.next
            second_node.next = first_node
            current.next = second_node
            
            current = first_node
        
        return dummy.next


sol = Solution()

h = [1,2,3,4,]


print(f"For {h} Nodes : {sol.swapPairs(h)}")
