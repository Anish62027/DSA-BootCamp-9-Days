
size = 5
deque = [None] * size
front = -1
rear = -1


def is_full(front, rear, size):
    return (front == 0 and rear == size - 1) or (front == rear + 1)


def is_empty(front, rear):
    return front == -1


def insert_front(deque, front, rear, size):
    if is_full(front, rear, size):
        print("Deque Overflow")
        return front, rear
    else:
        if front == -1: 
            front = 0
            rear = 0
        elif front == 0:  
            front = size - 1
        else:
            front -= 1
        value = int(input("Enter a number to insert at front :- "))
        deque[front] = value
        print(f"Deque : Inserted {value} at front")
    return front, rear


def insert_rear(deque, front, rear, size):
    if is_full(front, rear, size):
        print("Deque Overflow")
        return front, rear
    else:
        if front == -1: 
            front = 0
            rear = 0
        elif rear == size - 1:  
            rear = 0
        else:
            rear += 1
        value = int(input("Enter a number to insert at rear :- "))
        deque[rear] = value
        print(f"Deque : Inserted {value} at rear")
    return front, rear


def delete_front(deque, front, rear, size):
    if is_empty(front, rear):
        print("Deque Underflow")
        return front, rear
    else:
        remove = deque[front]
        deque[front] = None
        if front == rear:  
            front = -1
            rear = -1
        elif front == size - 1:
            front = 0
        else:
            front += 1
        print(f"Deque : Deleted {remove} from front")
    return front, rear


def delete_rear(deque, front, rear, size):
    if is_empty(front, rear):
        print("Deque Underflow")
        return front, rear
    else:
        remove = deque[rear]
        deque[rear] = None
        if front == rear:  
            front = -1
            rear = -1
        elif rear == 0:
            rear = size - 1
        else:
            rear -= 1
        print(f"Deque : Deleted {remove} from rear")
    return front, rear


def display(deque, front, rear, size):
    if is_empty(front, rear):
        print("Deque Underflow")
    else:
        print("Deque elements :- ", end=" ")
        i = front
        while i != rear:
            print(deque[i], end=" ")
            i = (i + 1) % size
        print(deque[rear])


while True:
    i = int(input('''
    ........ Enter Your Choice ........
    1. Insert at front
    2. Insert at rear
    3. Delete from front
    4. Delete from rear
    5. Display deque
    6. Exit
    ........ Choice Now Number ....... '''))

    if i == 1:
        front, rear = insert_front(deque, front, rear, size)
    elif i == 2:
        front, rear = insert_rear(deque, front, rear, size)
    elif i == 3:
        front, rear = delete_front(deque, front, rear, size)
    elif i == 4:
        front, rear = delete_rear(deque, front, rear, size)
    elif i == 5:
        display(deque, front, rear, size)
    elif i == 6:
        print("Exits program")
        break
    else:
        print("Invalid Choice , Please Enter Number Between 1 to 6.")
