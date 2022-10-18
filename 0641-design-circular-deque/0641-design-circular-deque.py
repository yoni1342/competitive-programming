class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.size = k
        
        
    def insertFront(self, value: int) -> bool:
        if len(self.deque)>=self.size:
            return False
        else:
            temp = []
            for i in range(len(self.deque)):
                temp.append(self.deque.pop())
            temp.append(value)
            for i in range(len(temp)):
                self.deque.append(temp.pop())
            return True
    def insertLast(self, value: int) -> bool:
        if len(self.deque)>=self.size:
            return False
        else:
            self.deque.append(value)
            return True
            
    def deleteFront(self) -> bool:
        if len(self.deque)==0:
            return False
        else:
            temp = []
            for i in range(len(self.deque)):
                temp.append(self.deque.pop())
            temp.pop()
            for i in range(len(temp)):
                self.deque.append(temp.pop())
            return True
        
    def deleteLast(self) -> bool:
        if len(self.deque)==0:
            return False
        else:
            self.deque.pop()
            return True

    def getFront(self) -> int:
        if len(self.deque)==0:
            return -1
        return self.deque[0]
        
    def getRear(self) -> int:
        if len(self.deque)==0:
            return -1
        return self.deque[len(self.deque)-1]

    def isEmpty(self) -> bool:
        if len(self.deque)==0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if len(self.deque)<self.size:
            return False
        else:
            return True
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()