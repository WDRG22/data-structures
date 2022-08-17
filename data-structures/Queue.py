from node import Node

class Queue:
    # A queue is a collection of data maintained in a sequence that can be modified by the addition of data at one end and the removal  from the other end
    
    def __init__(self):
        self.front = self.back = None
        self.size = 0
        
    def enqueue(self, data):
        # Insert element to back of the queue
        
        if self.back is None:
            self.back = self.front = Node(data)
            self.size += 1
            return
        
        new_node = Node(data)
        self.back.next = new_node
        self.back = new_node
        self.size += 1
        
    def dequeue(self):
        # Remove and return element from front of the queue 
        
        if self.front is None:
            print("Queue is empty")
            return
        
        res = self.front
        self.front = self.front.next
        
        if self.front is None:
            self.back = None
        
        self.size -= 1
        return res.data
        
    def show(self):
        # Print all elements of the queue
        
        if self.front is None:
            return
        
        current = self.front
        while(current):
            print(current.data, end=' -> ')
            current = current.next
        print("None")
    
    def isEmpty(self):
        return self.front is None
    
    
# TESTING 
greek = [
        "alpha", "beta", "gamma", "delta", "epsilon",
        "zeta", "eta", "theta", "iota", "kappa", 
        "lambda", "mu", "nu", "xi", "omicron", 
        "pi", "rho", "sigma", "tau", "upsilon",
        "phi", "chi", "psi", "omega"
        ]

myQueue = Queue()

for letter in greek:
    myQueue.enqueue(letter)
    
myQueue.show()
print(myQueue.size)
print(myQueue.dequeue())
print(myQueue.size)
myQueue.show()