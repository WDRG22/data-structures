from Node import Node
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
            
    def print_forward(self):
        for val in self.iter():
            print(val, end=' ')
        print()
            
    def print_reverse(self):
        for val in self.reverse_iter():
            print(val, end=' ')
        print()
            
    def get_count(self):
        return self.count
            
    def contains(self, data):
        # Search list for data, return boolean if found
        
        for val in self.iter():
            if val == data:
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
        # Delete node containing specified data from list and return its data
        # Return boolean if node deleted or not
        
        if self.head is None:
            return False
        elif self.head.data == data:
            self.delete_head()
            return True
        elif self.tail.data == data:
            self.delete_tail()
            return True
        else:
            current = self.head.next
            while current:
                if current.data == data:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    self.count -= 1
                    return True
                current = current.next
        return False
    
    def delete_head(self):
        # Delete head node and return its data
        # return None if no Node deleted
        
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
        # return None if no Node deleted 
        
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
  
  
  
# TESTING
  
greek = [
        "alpha", "beta", "gamma", "delta", "epsilon",
         "zeta", "eta", "theta", "iota", "kappa", 
         "lambda", "mu", "nu", "xi", "omicron", 
         "pi", "rho", "sigma", "tau", "upsilon",
         "phi", "chi", "psi", "omega"
        ]

myList = DoublyLinkedList()
for letter in greek:
    myList.append(letter)
    
print(myList.get_count()) #24
print(myList.contains("rho")) #true
myList.delete("rho")
print(myList.contains("rho")) #false
print(myList.delete_head())
print(myList.delete_tail())
print(myList.get_count()) #21

myList.insert("NEWHEAD")
myList.append("NEWTAIL")
myList.print_forward()