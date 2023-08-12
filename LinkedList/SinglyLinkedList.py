class Node:

    def __init__(self, value):
        self.value  = value
        self.next_node = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.sll_length = 0

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
        self.sll_length += 1

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

    def insert_at_location(self, loc, value):
        new_node = Node(value)
        temp_node = self.head
        temp_assist = None
        if self.head == None:
            if loc > 1:
                print("Invalid location. Please try again.")
            else:
                self.head = new_node
                self.tail = new_node
                self.sll_length += 1
        else:
            if(loc > self.sll_length + 1):
                print("Invalid location. Please try again.")
            else:
                count = 0
                while count <= loc:
                    if(count == loc - 1):
                        temp_assist.next_node = new_node
                        new_node.next_node = temp_node
                        break
                    count += 1
                    temp_assist = temp_node
                    temp_node = temp_node.next_node
                if(loc == self.sll_length + 1):
                    self.tail = new_node
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
    
    def search_value(self, value):
        temp_node = self.head
        node_found = False
        count = 1
        while count <= self.sll_length:
            if(temp_node.value == value):
                node_found = True
                break
            temp_node = temp_node.next_node
            count += 1
        if node_found == True:
            print(f"The value exists at node number {count}.")
        else:
            print("The value does not exists in the LinkedList.")
    

    def del_from_start(self):
        if self.head == None:
            print("The list is already empty.")
        else:
            self.head = self.head.next_node
            self.sll_length -= 1

    def del_from_end(self):
        if self.head == None:
            print("The list is already empty.")
        else:
            count = 1
            temp_node = self.head
            temp_assistant = None
            while count <= self.sll_length:
                if temp_node.next_node == None:
                    self.tail = temp_assistant
                    temp_assistant.next_node = None
                    break
                temp_assistant = temp_node
                temp_node = temp_node.next_node
                self.sll_length -= 1
    
    def del_from_loc(self, location):
        if self.head == None:
            print("The list is already empty.")
        elif location < 1 or location > self.sll_length:
            print("Invalid location. Please try again.")
        else:
            count = 1
            temp_node = self.head
            temp_assistant = self.head
            while count <= self.sll_length:
                if count == location:
                    temp_assistant.next_node = temp_node.next_node
                    break
                temp_assistant = temp_node
                temp_node = temp_node.next_node
                count += 1
            self.sll_length -= 1

    def del_by_val(self, val):
        if self.head == None:
            print("The list is already empty.")
        else:
            temp_node = self.head
            temp_assistant = self.head
            node_found = False
            count = 1
            while count <= self.sll_length:
                if temp_node.value == val:
                    temp_assistant.next_node = temp_node.next_node
                    node_found = True
                    break
                temp_assistant = temp_node
                temp_node = temp_node.next_node
                count += 1
            if(node_found == False):
                print("The value soes not exists in the List.")
            else:
                self.sll_length -= 1



sll = SinglyLinkedList()


operational_mistakes_count = 0

while operational_mistakes_count <= 3:
    operation = str(input("Please tell us, what to do? [insert/print/search/delete/exit]: "))
    if operation.lower() == "insert":
        print("You chosen insertion.")
        insertion_operational_mistakes_count = 0
        while insertion_operational_mistakes_count <= 3:
            insertion_operation_choice = str(input("Please tell us where to insert? [at_start/at_end/at_loc/exit]: "))
            if insertion_operation_choice.lower() == "at_start":
                value = int(input("Please enter the value to be inserted.: "))
                sll.insert_at_beginning(value)
            elif insertion_operation_choice.lower() == "at_end":
                value = int(input("Please enter the value to be inserted.: "))
                sll.insert_at_end(value)
            elif insertion_operation_choice.lower() == "at_loc":
                location = int(input("Please enter the location to insert the value.: "))
                if location < 1:
                    print("Invalid location. Please enter a valid location.")
                else:
                    value = int(input("Please enter the value to be inserted.: "))
                    sll.insert_at_location(location, value)
            elif insertion_operation_choice.lower() == "exit":
                print("Thank you. We would like to welcome you again!")
                break
            else:
                insertion_operational_mistakes_count += 1
                if insertion_operational_mistakes_count == 3:
                    print("Invalid input provided repeatedly. Terminating the code. ")
                    break
                print(f"Invalid operation. you have only {3 - insertion_operational_mistakes_count} chances to provide valid choice.")

    elif operation.lower() == "print":
        print("You chosen print")
        sll.print_ll()
    elif operation.lower() == "search":
        value = int(input("Please enter the value to search.: "))
        print("Let us search it for you.: ")
        sll.search_value(value)
    elif operation.lower() == "delete":
        deletion_operation_mistakes_count = 0
        while deletion_operation_mistakes_count < 3:
            deletion_operation_choice = str(input("Please tell us from where to delete the node? [from_start/from_end/from_location/by_value/exit]: "))
            if deletion_operation_choice.lower() == "from_start":
                sll.del_from_start()
            elif deletion_operation_choice.lower() == "from_end":
                sll.del_from_end()
            elif deletion_operation_choice.lower() == "from_location":
                loc = int(input("Please enter the location.: "))
                sll.del_from_loc(loc)
            elif deletion_operation_choice.lower() == "by_value":
                value = int(input("Please enter the value to be deleted from the LL.: "))
                sll.del_by_val(value)
                print("Deleting the value.")
            elif deletion_operation_choice.lower() == "exit":
                print("Exit")
                break
            else:
                deletion_operation_mistakes_count += 1
                if deletion_operation_mistakes_count == 3:
                    print("Invalid input provided repeatedly. Terminating the code. ")
                    break
                print(f"Invalid operation. you have only {3 - deletion_operation_mistakes_count} chances to provide valid choice.")
    elif operation.lower() == "exit":
        print("You chosen to exit.")
        break
    else:
        operational_mistakes_count += 1
        if operational_mistakes_count == 3:
            print("Invalid input provided repeatedly. Terminating the code. ")
            break

        print(f"Invalid operation. you have only {3 - operational_mistakes_count} chances to provide valid choice.")

    

# sll.insert_at_beginning(4)
# sll.insert_at_end(8)
# sll.insert_at_location(2, 6)
# sll.print_ll()

