class Node: 
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None

class LRU:
    def __init__(self):
        self.co = 0

    def has(self, data):
        if(ll.head == None):
            return False
        elif(ll.head.data == data):
            return True
        temp = ll.head.next
        while(temp):
            if(temp.data == data):
                return True
            temp = temp.next
        return False

    def dell(self, temp, data):
            temp = ll.head
            temp1 = ll.head
            if ll.head.data == data:
                ll.head = ll.head.next
            coun = 0
            while(temp):
                if temp.data == data:
                    break;
                temp = temp.next
                coun+=1
            for i in range(coun - 1):
                temp1 = temp1.next

    def put(self,data):
        if(self.has(data) == False):
            if(self.co >= 4):
                temp = ll.head.next
                ll.head = temp
                temp = ll.head
                while(temp.next):
                    temp = temp.next
                temp.next = Node(data)
            elif self.co == 0:
                ll.head = Node(data);
                self.co+=1
            else:
                temp = ll.head
                while(temp.next):
                    temp = temp.next
                temp.next = Node(data)
                self.co+=1
        else:
            temp = ll.head
            self.dell(temp, data)
            self.put(data)
        
    def get_cache(self):
        temp = ll.head 
        while (temp): 
            print(temp.data)
            temp = temp.next
    # def get(self, c):
if __name__ == '__main__':
    ll = LinkedList()    
    obj = LRU()
    obj.put(1)
    obj.put(2)
    obj.put(1)
    # obj.put(4)
    # obj.put(5)
    # obj.put(6)
    # obj.put(7)
    obj.get_cache()
