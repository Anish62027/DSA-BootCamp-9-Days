class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front 
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front 

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        if self.front == self.rear:  
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front  
        return data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.front:
                break
        print("[ back to front ]")

cir = Circular()

while True:
    choice = int(input('''
        ***** Enter a Number *****
        1. Insert 
        2. Delete 
        3. Display
        4. Exits Program

        Enter Your Choice -   '''))

    if choice == 1:
        data = int(input("Enter value  : "))
        cir.enqueue(data)
        print(f"Successfully Add Elements : {data} ")

    elif choice == 2:
        val = cir.dequeue()
        print(f"Successfully Delete element : {val}")

    elif choice == 3:
        print(f"Successfully Display ")
        cir.display()

    elif choice == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid Choice, Please Enter a Number Between 1 and 4")


