class Node:

    def __init__(self, value):
        self.value  = value
        self.next_node = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.sll_length = 0

    def insert_at_beginning(self, value):
        new_node = Node(value)
        temp_node = self.head
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
            while temp_node.next_node != None:
                temp_node = temp_node.next_node
            self.tail = temp_node
        self.sll_length += 1        
        
    def print_ll(self):
        temp_node = self.head
        count = 1
        print("Head")
        print("  | ")
        print("   -->", end = " ")

        while count <= self.sll_length:
            print(temp_node.value, end = " --> ")
            temp_node = temp_node.next_node
            count += 1
        print("None")

    def duplicate_remover(self):
        temp_node = self.head
        while temp_node != None:
            if temp_node.value == temp_node.next_node.value:
                temp_node.next_node = temp_node.next_node.next_node
                self.sll_length -= 1
            temp_node = temp_node.next_node
        
sll = SinglyLinkedList()

sll.insert_at_beginning(4)
sll.insert_at_beginning(4)
sll.insert_at_beginning(6)
sll.insert_at_beginning(8)
sll.insert_at_beginning(8)
sll.insert_at_beginning(9)
sll.duplicate_remover()
sll.print_ll()

