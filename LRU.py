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
    def init__(self, co):
        self.co = 0
    def put(self,data):
        if(has(data) == False):
            if(self.co >= 4):
                temp = head.next
                head = temp
                temp = head
                for i in range(3):
                    temp = temp.next
                temp = Node(data)
            elif self.co == 0:
                ll.head = Node(data);
                self.co++;
            else:
                temp = head
                for i in range(self.co):
                    temp = temp.next
                temp = Node(data)
                self.co++
        else:

    def has(self, data):
        if(head.data == data):
            return True
        temp = head.next
        for i in range(self.co - 1):
            if(temp.data == data):
                return True
            temp = temp.next
        return False
        
    def get_cache(self):

    def get(self, c):
