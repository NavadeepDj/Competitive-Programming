class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            new_node.prev = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            
            
        temp.next = new_node
        new_node.prev = temp
        print(new_node.prev.data)
        # print("tempvalue", temp.data)
        # print("tempNextValue", temp.next.data)
        new_node.next = self.head
        self.head.prev = new_node
        
        # print("new_node.nextValue", new_node.next.data)
        
    
    def printOut(self):
        temp = self.head
        print(self.head.data, end = "->")
        while temp.next != self.head:
            print(temp.next.data, end = "->")
            temp = temp.next
        print(temp.next.data)
        
    def reversePrint(self):
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            previ = temp
        print(temp.next.data, end = "->")    
        while previ != self.head:
            print(previ.data, end = "->")
            previ = previ.prev
        print(previ.data)
            
            
c1 = CircularLinkedList()
c1.insertAtEnd(1)
c1.insertAtEnd(2)
c1.insertAtEnd(3)
c1.printOut()
print()
c1.reversePrint()
