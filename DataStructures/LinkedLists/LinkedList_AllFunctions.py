class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #Empty at the start of LinkedList
    
    def insertAtBeginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        self.head = new_node
        new_node.next = temp
        
        # head -> insert(10) -> 20-> 30-> 40-> None
        
                
    def deleteAtbeginning(self):
        if self.head is None:
            print("Empty LinkedList")
        
        temp = self.head.next
        self.head = temp
        
    def deleteAtEnd(self):
        if not self.head:
            print("Empty LinkedList")
        temp = self.head
        while temp.next != None:
            prev = temp
            temp = temp.next
        prev.next = None
        
        # head -> 10 -> 20 -> 30 -> None
        
        
    def insertAtEnd(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node 
        # self.head.next = new_node

    def insertAtMiddle(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            l1.insertAtBeginning(data)
            return
        temp  = self.head
        for i in range(1, pos-1):
            temp = temp.next
        prev = temp.next
        temp.next = new_node
        # prev = prev.next
        new_node.next = prev
        
      
        # head -> 1 -> 10 -> insert(100) -> 20-> 30-> 40-> None
        
        # pos  -> 1 -> 2  -> 3           -> 4 -> 5 -> 6[We are trying to insert the element at pos 2; i.e., at 2nd element]
        
        
    def deleteAtMiddle(self, pos):
        if pos == 1:
            l1.deleteAtbeginning()
            return
        temp = self.head
        for i in range(1, pos):
            prev = temp
            temp = temp.next
        temp1 = temp.next
        prev.next = temp1
        
        
            
        
            
            
        
        
        
      
    def printOut(self):
        temp =self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print(None)
        
    def SearchForElement(self, data):
        temp = self.head
        booli = False
        while temp:
            if temp.data == data:
                # print("Found")
                booli = True
                break
            temp = temp.next
        if booli == True:
            print("Found")
        else:
            print("not found")

l1 = LinkedList()
l1.insertAtEnd(10)
l1.insertAtEnd(90)
l1.insertAtEnd(30)
l1.insertAtEnd(40)
l1.insertAtEnd(60)
# l1.deleteAtbeginning()
l1.insertAtMiddle(100, 1)
# l1.deleteAtEnd()
l1.deleteAtMiddle(2)

# # l1.printOut()
# data = int(input())
# while data != -1:
#     # l1.insertAtEnd(data)
#     # l1.insertAtBeginning(data)
#     l1.deleteAtbeginning() #No need for data input in deleteAtbeginning
#     data = int(input())
    
l1.printOut()
data1 = int(input("Searching element"))
l1.SearchForElement(data1)
