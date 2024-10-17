class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def is_empty(self):
        return self.head is None

    def push(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
            return
        else:
    
            self.tail.next = new_node
            self.tail = new_node


    def pop(self):
        if self.is_empty():
            print("Queue is UnderFlow")
            return -1 
        
        front = self.head.data
        if self.tail == self.head:
            self.tail = self.head = None
        
        else:
            self.head = self.head.next

        return front

    def peek(self):
        if self.is_empty():
            return -1
        
        return self.head.data


    def display(self):
        if self.is_empty():
            print("Queue is UnderFlow.")
        else:
            temp = self.head
            while temp!= None:
                print(temp.data, end=" ->")
                temp = temp.next
            print("null")  


stack = Stack()

while True:
    choice = int(input('''
        Enter a Number
        1. Push
        2. Pop
        3. Peek
        4. Display
        5. Exit

        Enter Your Choice '''))

    if choice == 1:
        data = int(input("Enter the value : "))
        stack.push(data)
        print(f"Successfully Push Elements : {data} ")
    elif choice == 2:
        pop = stack.pop()
        print(f"Successfully Pop Elements : {pop} ")
    elif choice == 3:
        top_element = stack.peek()
        print(f"Top Element : {top_element}")
    elif choice == 4:
        stack.display()
    elif choice == 5:
        print("Exit the stack operations.")
        break
    else:
        print("Invalid Choice, Please Enter a Number Between 1 and 5.")
