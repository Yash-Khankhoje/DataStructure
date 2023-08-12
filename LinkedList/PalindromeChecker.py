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

    def mid_finder(self):
        faster_temp = self.head
        slower_temp = self.head
        mid_node = slower_temp
        while faster_temp.next_node != None:
            faster_temp = faster_temp.next_node
            if faster_temp.next_node != None:
                faster_temp = faster_temp.next_node
                slower_temp = slower_temp.next_node
                mid_node = slower_temp
        return mid_node

    def half_reversal(self, node):
        prev = node
        curr = node.next_node
        while curr != None:
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next

        node.next_node = None
        second_head = prev
        return second_head
    
    def palindrom_checker(self):
        mid = self.mid_finder()
        tail_node = self.half_reversal(mid.next_node)
        temp_node = self.head

        while tail_node.next_node != None:
            if tail_node.value != temp_node.value:
                return False
            tail_node = tail_node.next_node
            temp_node = temp_node.next_node
        return True

                        

        print(mid_node.value)
        # return mid_node.value
        
sll = SinglyLinkedList()

sll.insert_at_beginning(1)
sll.insert_at_beginning(2)
sll.insert_at_beginning(3)
# sll.insert_at_beginning(3)
sll.insert_at_beginning(2)
sll.insert_at_beginning(1)
sll.print_ll()
print(sll.palindrom_checker())

