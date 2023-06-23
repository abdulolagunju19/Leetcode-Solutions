class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    """
    Optimal Time Complexity: O(n)
    Corresponding Space Complexity: O(1)
        - Algorithm: fast pointer moves by two and catches slow pointer if the list has a cycle
    """
    def hasCycle(self, head: [ListNode]) -> bool:
        fast,slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

