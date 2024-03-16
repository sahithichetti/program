class listnode:
    def __init__(self,x):
        self.val=x
        self.next=None
class solution:
    def deletenode(self,node):
        node.val=node.next.val
        node.next=node.next.next
