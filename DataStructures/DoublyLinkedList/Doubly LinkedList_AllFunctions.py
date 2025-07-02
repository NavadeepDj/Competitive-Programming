'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Node:
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
        
    
    def insertAtBeginning(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        temp =self.head
        self.head = new_node
        
        new_node.next = temp
        temp.prev = new_node
        
    
    def deleteAtBeginning(self):
        temp = self.head
        self.head = temp.next
        self.head.prev = None
        
    def deleteAtEnd(self):
        temp = self.head
        while temp.next != None:
            previ = temp
            temp = temp.next
        previ.next = None
        temp.prev = previ
        
        
    def insertAtMiddle(self, data, pos):
        new_node = Node(data)
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        temp1 = temp.next
        temp.next = new_node
        new_node.prev = temp
        
        new_node.next = temp1
        temp1.prev = new_node
        
    
        # head -> 1 -> 10 -> insert(10) -> 20-> 30-> 40-> None
        
        # pos  -> 1 -> 2  -> 3           -> 4 -> 5 -> 6[We are trying to insert the element at pos 3; i.e., at 3rd element]
        
    
    def deleteAtMiddle(self, pos):
        temp = self.head
        for i in range(1, pos):
            previ = temp
            temp = temp.next
        
        temp1 = temp.next
        previ.next = temp1
        temp1.prev = previ
       
        # temp2 = self.head
        # for i in range(1, pos-1):   #Error
                                      #Error
        #     temp2 = temp2.next
        # temp2.next = temp1
        # temp1.prev = temp2
        
        # 1->2->3->4>None
    
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
d1.insertAtEnd(4)
# d1.insertAtBeginning(1)
# d1.insertAtBeginning(4)
# d1.insertAtBeginning(2)
# d1.deleteAtBeginning()
# d1.insertAtMiddle(10, 3)
d1.deleteAtMiddle(2)
# d1.deleteAtEnd()


d1.printOut()
print()
d1.printReverse()

        
        
