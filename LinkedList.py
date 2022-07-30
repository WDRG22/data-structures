class Node:
    def __init__(self, value, next_node, prev_node):
        self.value = value
        self.next = next_node
        self.prev = prev_node
        
    def __str__(self):
        return str(self.value)
        
class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        
        if values is not None:
            self.add_nodes(values)
        
    def __str__(self):
        return '->'.join([str(node) for node in self])
    
    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count +=1
            curr = curr.next
        return count
    
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
        
    # Adds node to end of list, returns new tail
    def add_node(self, value):
        if self.head is None:
            self.head = self.tail = Node(value, None, None)
        else:
            self.tail.next = Node(value, None, self.tail)
            self.tail = self.tail.next
        return self.tail
    
    # Adds list of nodes to end of list, returns new tail
    def add_nodes(self, values):
        for value in values:
            self.add_node(value)
        return self.tail
            
    # Adds node to head of list, returns new head        
    def add_node_as_head(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            self.head.prev = Node(value, self.head, None)
            self.head = self.head.prev
        return self.head
    
    # Adds list of nodes to front of list (in reverse order)
    # i.e. last element of values becomes new head
    def add_nodes_to_head(self, values):
        for value in values:
            self.head = self.add_node_as_head(value)
        return self.head
    
    def remove_head(self):
        res = self.head
        self.head = self.head.next
        self.head.prev = None
        return res
    
    def remove_tail(self):
        res = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return res