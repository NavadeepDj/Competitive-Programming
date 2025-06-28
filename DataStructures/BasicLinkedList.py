class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None #Empty at the start of likedist'
        
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
        
    def printOut(self):
        
        temp =self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print(None)

l1 = LinkedList()
l1.insertAtEnd(10)
l1.insertAtEnd(90)
l1.insertAtEnd(30)
l1.insertAtEnd(40)

l1.printOut()
