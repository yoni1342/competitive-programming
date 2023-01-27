class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.dummy = Node('x')

    def get(self, index: int) -> int:
        count=0
        cur = self.dummy.next
        while cur and count!=index:
            cur = cur.next
            count+=1
        if not cur:
            return -1
        return cur.val

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        temp = self.dummy.next
        self.dummy.next = node
        node.next = temp
    def addAtTail(self, val: int) -> None:
        node = Node(val)
        cur = self.dummy
        while cur.next != None:
            cur = cur.next
        cur.next = node
        
    def addAtIndex(self, index: int, val: int) -> None:
        count = 0
        cur = self.dummy
        node = Node(val)
        
        while cur and count!=index:
            cur = cur.next
            count+=1
        if not cur:
            return -1
        temp = cur.next
        cur.next = node
        node.next = temp

    def deleteAtIndex(self, index: int) -> None:
        count = 0
        cur = self.dummy
      
        while cur and count<index:
            cur = cur.next
            count+=1
        if not cur:
            return -1
        if cur.next:
            cur.next = cur.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)