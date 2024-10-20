class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def add_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def remove_front(self):
        if self.is_empty():
            print("DEQUE Is Empty")
            return -1
        
        data = self.head.data
        if self.head == self.tail:  
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data

    def remove_rear(self):
        if self.is_empty():
            print("DEQUE Is Empty")
            return -1
        
        data = self.tail.data
        if self.head == self.tail:  
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data

    def display(self):
        if self.is_empty():
            print("Deque is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("Null")


deque = Deque()

while True:
    choice = int(input('''
        ***** Enter a Number *****
        1. Insert Into Front
        2. Insert Into Rear
        3. Delete Into Front
        4. Delete Into Rear
        5. Display Deque
        6. Exits Program

        Enter Your Choice -   '''))

    if choice == 1:
        data = int(input("Enter value to insert at the Front : "))
        deque.add_front(data)
        print(f"Successfully Add Elements at the Front : {data} ")

    elif choice == 2:
        data = int(input("Enter value to insert in the Rear : "))
        deque.add_rear(data)
        print(f"Successfully Add Elements at the Rear : {data} ")

    elif choice == 3:
        val = deque.remove_front()
        if val == -1:
            print("No element delete")
        else :
            print(f"Successfully Delete element from Front : {val}")

    elif choice == 4:
        val = deque.remove_rear()
        if val == -1:
            print("No element delete")
        else :
            print(f"Successfully Delete  element from Rear : {val}")

    elif choice == 5:
        print(f"Successfully Display Deque Using Linked-List")
        deque.display()

    elif choice == 6:
        print("Exiting the program.")
        break

    else:
        print("Invalid Choice, Please Enter a Number Between 1 and 8.")

