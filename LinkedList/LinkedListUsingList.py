class SinglyLinkedList:
    def __init__(self):
        self.lst = []
        self. ll_lenth = 0

    def insert_at_end(self, val):
        self.lst.append(val)
        self.ll_lenth += 1
        print(self.lst)

    def insert_at_start(self, val):
        self.lst.insert(0,val)
        self.ll_lenth += 1
        print(self.lst)

    def insert_at_loc(self, loc, val):
        if self.ll_lenth == 0:
            if loc > 1:
                print("Invalid location. Please provide a valid location.")
            else:
                self.lst.insert(0, val)
                self.ll_lenth += 1
        else:
            if loc > self.ll_lenth + 1 or loc < 1:
                print("Invalid location. Please provide a valid location.")
            else:
                self.lst.insert(loc - 1, val)
                self.ll_lenth += 1
        print(self.lst)

    def del_from_start(self):
        if self.ll_lenth == 0:
            print("The list is already empty. ")
        else:
            self.lst.pop(0)
            self.ll_lenth -= 1
        print(self.lst)

    def del_from_end(self):
        if self.ll_lenth == 0:
            print("The list is already empty. ")
        else:
            self.lst.pop()
            self.ll_lenth -= 1
        print(self.lst)

    def del_from_loc(self, loc):
        if self.ll_lenth == 0:
            print("The list is already empty. ")
        elif loc < 1 or loc > self.ll_lenth:
            print("Invalid location. Please provide valid location.: ")
        else:
            self.lst.pop(loc-1)
            self.ll_lenth -= 1
        print(self.lst)

    def del_by_val(self, val):
        if self.ll_lenth == 0:
            print("The list is already empty. ")
        else:
            if val in self.lst:
                self.lst.remove(val)
                self.ll_lenth -= 1
            else:
                print("Value does not exists in the list.")
        print(self.ll_lenth)

    def search_val(self, val):
        if self.ll_lenth == 0:
            print("The list is already empty. ")
        else:
            if val in self.lst:
                print(f"The value exist at node number{self.lst.index(val) + 1}")
            else:
                print("The value does not exists in the list.")




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
                sll.insert_at_start(value)
            elif insertion_operation_choice.lower() == "at_end":
                value = int(input("Please enter the value to be inserted.: "))
                sll.insert_at_end(value)
            elif insertion_operation_choice.lower() == "at_loc":
                location = int(input("Please enter the location to insert the value.: "))
                value = int(input("Please enter the value to be inserted.: "))
                sll.insert_at_loc(location, value)
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

 

     
        





