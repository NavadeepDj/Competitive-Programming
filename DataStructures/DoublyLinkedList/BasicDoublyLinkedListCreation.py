class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        
        while temp.next != None:
            prev = temp
            temp = temp.next
            
        temp.next = new_node
        temp.prev = None
        
    
    def printOut(self):
        
        temp = self.head
        while temp!= None:
            print(temp.data, end = " -> ")
            temp = temp.next
            
        print(None)
            
        
        
        
        
    # head -> <-10 -> <- 20 -> <- 30 -> <-None
        
       

d1 = DoublyLinkedList()
# data = int(input())
d1.insertAtEnd(1)
d1.insertAtEnd(2)
d1.insertAtEnd(3)


d1.printOut()

        
        


