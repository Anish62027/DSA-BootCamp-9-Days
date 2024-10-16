
size = 4
queue = [None] * size
front = -1
rear = -1

def is_full(front, rear, size):
    return (rear + 1) % size == front

def is_empty(front, rear):
    return front == -1


def enqueue(queue, size, front, rear):
    if is_full(front, rear, size):
        print("Queue Overflow")
        return front, rear
    else:
        if front == -1:
            front = 0
        rear = (rear + 1) % size
        a = int(input("Enter a number : "))
        queue[rear] = a
        print(f"Enqueued {a} into the queue")
        return front, rear


def dequeue(queue, front, rear):
    if is_empty(front, rear):
        print("Queue Underflow")
        return front, rear
    else:
        a = queue[front]
        queue[front] = None  
        if front == rear:  
            front = -1
            rear = -1
        else:
            front = (front + 1) % size
        print(f"Dequeued {a} from the queue")
        return front, rear


def display(queue, front, rear, size):
    if is_empty(front, rear):
        print("Queue is empty!")
    else:
        print("Queue elements are:")
        i = front
        while i != rear:
            print(queue[i],end=",")
            i = (i + 1) % size
        print(queue[rear])  


while True:
    i = int(input('''
    ........ Enter Your Choice ........
    1. Enqueue
    2. Dequeue
    3. Display
    4. Exit
    ........ Choice Now Number ....... '''))

    if i == 1:
        front, rear = enqueue(queue, size, front, rear)
    elif i == 2:
        front, rear = dequeue(queue, front, rear)
    elif i == 3:
        display(queue, front, rear, size)
    elif i == 4:
        print("Exits the program")
        break
    else:
        print("Invalid choice, please try again.")
