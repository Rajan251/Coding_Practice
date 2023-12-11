queue = []
def enqueue():
    element = input("enter the element:")
    queue.append(element)
    print(element,'is added to queue!')

def dequeue():
    if not queue:
        print("queue is empty!")
    else:
        e=queue.pop(0)
        print("removed element:",e)

def display():
    print(queue)

while True:
    print("Select the operation 1.add 2.remove 3.display 4.quit")
    choice = int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct options")

    






# enqueue: to add element in the  queue using append method
# dequeue: pop method to removed the element using pop method
# two part are present in the Queue back or rear/tail and second one is called front/head of the queue.
# two method are used FIFO LIFO
#  