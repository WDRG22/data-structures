from Node import Node
        
class Stack:
    
    def __init__(self, head=None):
        self.head = head
        self.count = 0

    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.count += 1
        
    def pop(self):        
        if self.head is None:
            print("Stack empty")
            return 
    
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data
    
    def peek(self):
        if self.head is None:
            print("Stack empty")
        
        return self.head.data
        
    def show(self):
        if self.head is None:
            print("Stack empty")
            return
        
        current = self.head
        while (current):
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def length(self):
            return self.count
        
    def isEmpty(self):
        return self.count == 0
    
    
# TESTING
greek = [
        "alpha", "beta", "gamma", "delta", "epsilon",
         "zeta", "eta", "theta", "iota", "kappa", 
         "lambda", "mu", "nu", "xi", "omicron", 
         "pi", "rho", "sigma", "tau", "upsilon",
         "phi", "chi", "psi", "omega"
        ]
greek.reverse()
myStack = Stack()

for letter in greek:
    myStack.push(letter)
    
myStack.show()
print(myStack.pop())
print(myStack.length())