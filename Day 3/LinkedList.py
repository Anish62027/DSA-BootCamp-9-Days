class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head == None
    
    def add_into_beg(self, data):
        new_node = Node(data)
        self.size+=1
        if self.head == None:
            self.head = self.tail = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
    
    def add_into_med(self, data , pos):
        new_node = Node(data)
        self.size+=1
        current_node = self.head
        for _ in range(pos - 1): 
            current_node = current_node.next
        new_node.next = current_node.next  
        current_node.next = new_node


    def add_into_end(self,data):
        new_node = Node(data)
        self.size+=1
        if self.head == None:
            self.head = self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node

    def del_into_beg(self):
        if self.size == 0:
            print("Linked List is UnderFlow")
            return -1
        
        elif self.size == 1:
            val = self.head.data
            self.head = self.tail = None
            self.size = 0
            return val
        
        val = self.head.data
        self.head.next
        self.size -=1
        return val
    
    def del_into_mid(self , pos):

        if self.size == 0:
            print("Linked List is UnderFlow")
            return -1

        if pos == 1:
            return self.del_into_beg()
        
        curr_val = self.head
        for i in range(pos - 2): 
            curr_val = curr_val.next

        val = curr_val.next.data  
        curr_val.next = curr_val.next.next  
        self.size -= 1
        
        if pos == self.size + 1: 
            self.tail = curr_val
        
        return val
    

    def del_into_end(self):
        if self.size == 0:
            print("Linked is UnderFlow")
            return -1
        
        elif self.size == 1:
            val = self.head.data
            self.head = self.tail = None
            self.size = 0
            return val
        
        i = self.size-2
        prev = self.head

        for i in range(0,self.size):
            prev = prev.next
        
        val = prev.next.data
        prev.next =None
        self.tail = prev
        self.size -=1
        return val
    
    def display(self):
        if self.is_empty():
            print("Linked is UnderFlow")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("null") 



linkedlist = LinkedList()

while True:
    choice = int(input('''
        ***** Enter a Number *****
        1. Insert Into Begning
        2. Insert Into Mid
        3. Insert Into End
        4. Delete Into Begning
        5. Delete Into Mid
        6. Delete Into End
        7. Display Linked-List
        8. Exits Program

        Enter Your Choice :-  '''))

    if choice == 1:
        data = int(input("Enter value to insert at the beginning Data : "))
        linkedlist.add_into_beg(data)
        print(f"Successfully Add Elements at the beginning : {data} ")

    elif choice == 2:
        data = int(input("Enter value to insert in the middle Data : "))
        pos = int(input("Enter the position: "))
        linkedlist.add_into_med(data, pos)
        print(f"Successfully Add Elements at the Middle : {data} ")

    elif choice == 3:
        data = int(input("Enter value to insert at the end Data : "))
        linkedlist.add_into_end(data)
        print(f"Successfully Add Elements at the End : {data} ")

    elif choice == 4:
        val = linkedlist.del_into_beg()
        if val == -1:
            print("No element delete")
        else :
            print(f"Successfully Delete element from beginning : {val}")
            
    elif choice == 5:
        pos = int(input("Enter the position to delete from: "))
        val = linkedlist.del_into_mid(pos)
        if val == -1:
            print("No element delete")
        else :
            print(f"Successfully Deleted element from position {pos}: {val}")

    elif choice == 6:
        val = linkedlist.del_into_end()
        if val == -1:
            print("No element delete")
        else :
            print(f"Successfully Delete  element from End : {val}")

    elif choice == 7:
        print(f"Successfully Display Linked-List")
        linkedlist.display()

    elif choice == 8:
        print("Exiting the program.")
        break

    else:
        print("Invalid Choice, Please Enter a Number Between 1 and 8.")


    