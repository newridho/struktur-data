#Tambahkan method pada Class Queue yang berfungsi untuk melakukan dequeue pada posisi ke-x di dalam Queueu, di mana posisi ke-x dihitung dari last of queue. Beri nama method ini desperation().
#Queue == antrian, equeue == menambah antrian, dequeue == menghapus antrian, despiration == mengambil elemen pertama.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end="-> ")
            temp = temp.next
        print("None")
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp
    
    def desperation(self, x):
        if x < 1 or x > self.length:
            return None
        if x == self.length:
            return self.dequeue()
        temp = self.first
        for _ in range(self.length - x - 1):
            temp = temp.next
        node_to_remove = temp.next
        temp.next = node_to_remove.next
        node_to_remove.next = None
        self.length -= 1
        return node_to_remove

myQueue = Queue(1)
print('Queue before enqueue(2):')
myQueue.print_queue()

myQueue.enqueue(2)
print('Queue after enqueue(2):')
myQueue.print_queue()

print(myQueue.dequeue().value)
print(myQueue.dequeue().value)
print(myQueue.dequeue())
# print('Queue after dequeue():')
# myQueue.print_queue()

myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
print('Queue after enqueue():')
myQueue.print_queue()

print(myQueue.desperation(2).value)
print(myQueue.desperation(1).value)
print(myQueue.desperation(3))
print('Queue after desperation():')
myQueue.print_queue()