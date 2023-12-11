class Node:
    def __init__(self, data=None,next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def Insert_at_beginig(self, data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def Insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        irt = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.Insert_at_end(data)

    def get_length(slef):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        
        return count

    def remove_at(self, index):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = slef.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.Insert_at_beginig(5)
    ll.Insert_at_beginig(89)
    ll.remove_at(2) # remove 2 value from linked list
    ll.remove_at(20) # throw exception
    ll.insert_at(0,"figs") # insert value from 0 index
    ll.print()
     
