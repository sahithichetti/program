def oddeven(self,head):
    oddhead=head
    evenhead=head.next
    odd=oddhead
    even=evenhead
    while even and even.next:
        odd.next=even.next
        odd=odd.next
        even.next=odd.next
        even=even.next
    odd.next=evenhead
    self.head=oddhead
    self.show()
