class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def display(self):
        temp = self.head 
        while temp:
            print(temp.value, end="-> ")
            temp = temp.next
        print("Selesai")
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length+=1
        return True
    
    def pulang(self):
        temp = self.tail
        while temp:
            print(temp.value, end="-> ")
            temp = temp.prev
        print("Selesai")
    
myDoublyLinkedList = DoublyLinkedList("UTY")
myDoublyLinkedList.append("Jl. Magelang")
myDoublyLinkedList.append("Jl. Mangkubumi")
myDoublyLinkedList.append("Tugu Jogja")
myDoublyLinkedList.display()
myDoublyLinkedList.pulang()

    
