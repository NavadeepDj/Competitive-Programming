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
            # return # due to this infinite loop exists;;
        temp = self.head
        self.head = new_node
        new_node.next = temp
        
        
        # head -> insert(10) -> 20-> 30-> 40-> None
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
# l1.insertAtEnd(10)
# l1.insertAtEnd(90)
# l1.insertAtEnd(30)
# l1.insertAtEnd(40)

# l1.printOut()
data = int(input())
while data != -1:
    # l1.insertAtEnd(data)
    l1.insertAtBeginning(data)
    data = int(input())
    
l1.printOut()
data1 = int(input("Searching element"))
l1.SearchForElement(data1)
