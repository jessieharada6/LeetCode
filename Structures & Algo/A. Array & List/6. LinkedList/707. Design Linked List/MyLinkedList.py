class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class MyLinkedList(object):
    def __init__(self):
        self.head = self.tail = Node(-1) 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index) -> int:
        node = self.getNode(index)
        return node.val if node else -1
    
    def getNode(self, index: int) -> Node | None:
        isLeft = index < self.size / 2
        if not isLeft:
            index = self.size - index - 1
        
        cur = self.head.next if isLeft else self.tail.prev
        while cur != self.head or cur != self.tail:
            if index == 0: return cur
            cur = cur.next if isLeft else cur.prev
            index -= 1
        return None
        
    def addAtHead(self, val):
        node = Node(val)
        
        node.next = self.head.next
        node.prev = self.head
        
        self.head.next.prev = node
        self.head.next = node
        
        self.size += 1


    def addAtTail(self, val):
        node = Node(val)
        
        node.next = self.tail
        node.prev = self.tail.prev
        
        self.tail.prev.next = node
        self.tail.prev = node
        
        self.size += 1

        
    def addAtIndex(self, index, val):
        if index > self.size: return
        if index <= 0: self.addAtHead(val)
        elif index == self.size: self.addAtTail(val)
        else:
            cur = self.getNode(index)
            node = Node(val)
            
            prev = cur.prev

            prev.next = node
            node.next = cur
            cur.prev = node
            node.prev = prev
        
            self.size += 1
        

    def deleteAtIndex(self, index):
        cur = self.getNode(index)
        
        if cur:
            prev = cur.prev
            next = cur.next
            
            prev.next = next
            next.prev = prev
            cur.next = cur.prev = None

            self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)