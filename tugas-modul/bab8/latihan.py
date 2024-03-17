# Tambahkan method pada Class Stack yang berfungssi untuk melakukan Push setelah elemen ke-i pada Stack dengan ketentuan Nilai i dihitung dari bottom of stack. Beri nama method ini sisip_stack().

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value, end="-> ")
            temp = temp.next
        print("None")
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    def sisip_stack(self, value, i):
        if i <= 0:
            self.push(value)
        elif i >= self.height:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
            self.height += 1
        else:
            temp = self.top
            for _ in range(self.height - i - 1):
                temp = temp.next
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.height += 1

my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print('Stack before pop():')
my_stack.print_stack()

print('\nPooped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()

print('\nStack after sisip_stack():')
my_stack.sisip_stack(9, 2)
my_stack.sisip_stack(8, 1)
my_stack.print_stack()