
size = 5
l = []

def push(l, size):
    
    if len(l) == size:
        print("Stack Overflow")
    else:
        a = int(input("Enter a Number: "))
        l += [a]
        print(f"Number {a} has been successfully pushed")

def pop(l):
    if len(l) == 0:
        print("Stack Underflow")
    else:
        a = l[-1]  
        l = l[:-1]
        print(f"Stack {a} has successfully popped")
        return l 
    
def display(l):
    if len(l) == 0:
        print("Stack Underflow")
    else:
        print("Stack:", l) 

while True:
    i=int(input('''
        Enter a Number 
        1. push
        2. pop
        3. Display
        4. exit
        
        Enter Your Choice :- '''))
    
    
    
    
    if i==1:
        push(l,size)
    elif i==2:
        l= pop(l)
    elif i==3:
        display(l)
    elif i==4:
        print("Stack has Exits..")
    else:
        print("Invalid Choice , Please Enter Number Between 1 to 4")