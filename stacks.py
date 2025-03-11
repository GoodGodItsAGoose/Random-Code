import random as r
import node as n
class Stack:
    def __init__(self):
        self.items = []
        self.ll = n.linked_list()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty."
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty."
    
    def size(self):
        return len(self.items)
    
    def display(self):
        for _ in range(self.size()):
            print(self.peek(), end = " | ")
            self.pop()
    
    def save(self):
        if self.check(self.items) == True:
            return
        self.ll.insert_at_beginning(self.items)
        self.items = []
        
    def clear(self):
        self.items = []
    
    def load(self, stackIndex):
        loaded_stack = self.ll.find_node_index(stackIndex)
        self.items = loaded_stack
    
    def check(self, stack):
        num = 1
        for _ in range(self.ll.length()):
            if stack == self.ll.find_node_index(num):
                return True
            else:
                num += 1
        return False
