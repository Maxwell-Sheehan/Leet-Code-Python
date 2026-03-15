# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head # set everything equal to the head of the linked list
        while fast and fast.next: #while fast and fast.next are both still valid 
            fast = fast.next.next #fast moves forward two spaces
            slow = slow.next #slow moves forward one space

        return slow #when the list ends slow is going to be in teh middle
        