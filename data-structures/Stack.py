from node import Node
     
class Stack:
    
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def push(self, data):
        # Push new data onto top of stack
        
        new_node = Node(data, self.head)
        self.head = new_node
        self.count += 1
        
    def pop(self):
        # Pop top element off of stack and return it
         
        if self.head is None:
            print("Stack empty")
            return 
    
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data
    
    def peek(self):
        # Return current top element
        
        if self.head is None:
            print("Stack empty")
        
        return self.head.data
        
    def show(self):
        # Print entire stack
        
        if self.head is None:
            print("Stack empty")
            return
        
        current = self.head
        while (current):
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def length(self):
        # Return stack size
        
            return self.count
        
    def isEmpty(self):
        # Return if stack is empty
        
        return self.count == 0
    
    
# TESTING
greek = [
        "alpha", "beta", "gamma", "delta", "epsilon",
        "zeta", "eta", "theta", "iota", "kappa", 
        "lambda", "mu", "nu", "xi", "omicron", 
        "pi", "rho", "sigma", "tau", "upsilon",
        "phi", "chi", "psi", "omega"
        ]

myStack = Stack()

for letter in greek:
    myStack.push(letter)
    
myStack.show()
print(myStack.pop())
print(myStack.length())