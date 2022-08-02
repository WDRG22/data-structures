class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def iter(self):
        # Iterate forwards through the list
        
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
        
    def reverse_iter(self):
        # Iterate backwards through the list
        
        current = self.tail
        while current:
            val = current.data
            current = current.prev
            yield val
            
    def contains(self, data):
        # Search list for data, return boolean if found
        
        for val in self.iter():
            if data == val:
                return True
            return False
        
    def append(self, data):
        # Append data to end of list

        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        
    def insert(self, data):
        # Insert data to front of list
        
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1
        
    def delete(self, data):
        # Delete node containing specified data from list
        
        return
    
    def delete_head(self):
        # Delete head node and return its data
        
        if self.head is None:
            return None
        else:
            val = self.head.data
            self.head = self.head.next
            self.count -= 1
            try:
                self.head.prev = None
            except:
                pass
        return val
    
    def delete_tail(self):
        # Delete tail node and return its data 
        
        if self.tail is None:
            return None
        else:
            val = self.tail.data
            self.tail = self.tail.prev
            self.count -= 1
            try:
                self.tail.next = None
            except:
                pass
        return val