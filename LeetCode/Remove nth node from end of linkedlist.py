"""
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        for _ in range(n+1):
            first=first.next
        
        while first:
            second=second.next
            first=first.next
        
        second.next=second.next.next

        return dummy.next
        
