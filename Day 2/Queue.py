

size = 5
l = [None] * size
front = 0
rear = -1

def push(l, size, rear):
        
    if rear == size - 1:
        print("Queue Overflow")
    else:
        a = int(input("Enter a Number: "))
        rear += 1
        l[rear] = a
        print(f"Number {a} has been successfully pushed Queue")
    return rear


def pop(l, front, rear):
    if front > rear:
        print("Queue Underflow")
    else:
        a = l[front]
        front += 1
        print(f"Number {a} has been successfully popped Queue")
    return front

    

def display(l, front, rear):
    if front > rear:
        print("Queue Underflow")
    else:
        print("Queue elements are:")
        for i in range(front, rear + 1):
            print(l[i])


while True:
    
    
    i=int(input('''
        Enter a Number 
        1. Enqueue
        2. DeQueue
        3. Display
        4. exit
        
        Enter Your Choice :- '''))
    
    
    if i == 1:
        rear = push(l, size, rear)
    elif i == 2:
        front = pop(l, front, rear)
    elif i == 3:
        display(l, front, rear)
    elif i == 4:
        print("Exiting the Queue program")
        break
    else:
        print("Invalid Choice. Please Enter a Number Between 1 and 4.")