'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
            temp = temp.next
            
        temp.next = new_node
        new_node.prev = temp
        
    
    def printOut(self):
        
        temp = self.head
        while temp!= None:
            print(temp.data, end = "->")
            previ = temp
            temp = temp.next
        print(None)
        
    
    def printReverse(self):
        
        temp = self.head
        while temp!= None:
            # print(temp.data, end = " -> ")
            previ = temp
            temp = temp.next
            
            # print(temp.data)
    
        # temp = temp.prev   
        while previ != None:
            print(previ.data, end = "->")
            previ = previ.prev
        print(None)
        
        
    # head -> <-10 -> <- 20 -> <- 30 -> <-None
        
       

d1 = DoublyLinkedList()
# data = int(input())
d1.insertAtEnd(1)
d1.insertAtEnd(2)
d1.insertAtEnd(3)


d1.printOut()
print()
d1.printReverse()

        
        
