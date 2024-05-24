# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Get values of current nodes or 0 if node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum of current digits and carry
            total = val1 + val2 + carry
            carry = total // 10  # Calculate carry for next iteration
            digit = total % 10   # Calculate digit to append to result

            # Create new node with the calculated digit
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes in the linked lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next
