class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None


    def print_reverse(self, node):
        if node is None:
            return -1
        self.print_reverse(node.next)
        print(node.data, end=" -> ") 
    
    def print_list_reverse(self):
        self.print_reverse(self.head)
        print("Null")

    
    def is_empty(self):
        return self.head is None

    def push(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        else:
    
            new_node.next = self.head
            self.head = new_node


    def pop(self):
        if self.is_empty():
            return -1 
        
        top = self.head.data
        self.head = self.head.next
        return top

    def peek(self):
        if self.is_empty():
            return -1
        
        return self.head.data


    def display(self):
        if self.is_empty():
            print("Stack is UnderFlow.")
        else:
            temp = self.head
            while temp!= None:
                print(temp.data, end=" ->")
                temp = temp.next
            print("null")  


stack = Stack()

while True:
    choice = int(input('''
        Enter a Number:
        1. Push
        2. Pop
        3. Peek
        4. Display
        5. Reverse
        6. Exit

        Enter Your Choice: '''))

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
        stack.print_list_reverse()
        print("Successfully Reverse ")
    elif choice ==6:
        print("Exiting the stack operations.")
        break
    else:
        print("Invalid Choice, Please Enter a Number Between 1 and 5.")
