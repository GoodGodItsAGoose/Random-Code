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


        

cards = [
    "spades",
    "diamonds",
    "hearts",
    "clovers"
]
# stack = Stack()
# def makeCards():
#     num = 1
#     num2 = 0
#     fullCards = []
#     for _ in range(4):
#         num = 1
#         for _ in range(10):
#             card = str(num) + " of " + cards[num2]
#             fullCards.append(card)
#             num += 1
#         num2 += 1
#     num = 0
#     r.shuffle(fullCards)
#     for _ in range(40):
#         stack.push(fullCards[num])
#         num += 1
# makeCards()
# print("First save")
# stack.save()
# print(stack.peek())
# num = 0
# for _ in range(16):
#     stack.push(num)
#     num += 1
# print("second save and display")
# stack.save()
# stack.ll.display()
# print("loading 2")
# stack.load(2)
# print(stack.peek())
# stack.ll.display()
# print("loading 1")
# stack.load(1)
# print(stack.peek())
# stack.clear() # this is needed for whatever reason
# num = 256
# for _ in range(16):
#     stack.push(num)
#     num += 1
# print("fourth save and display")
# stack.save()
# stack.load(1)
# print(stack.peek())
# stack.ll.display()
# print(stack.peek()) # returns 80
# stack.pop() # removes 80
# print(stack.peek()) # returns 70

# player1Hand = []
# player2Hand = []

# def drawCard(playerHand):
#     playerHand.append(stack.peek())
#     stack.pop()

# drawCard(player1Hand)
# print(player1Hand)