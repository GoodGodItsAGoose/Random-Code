class Node:
    # [node | next]
    def __init__(self, data):
        self.data = data
        # [node = data]
        self.next = None
        # [next = none]
        
# [Head pointer ->  current head  ->      tail      -> none]
# [    head     ->   [(10)-->]    ->   [(20)-->]    -> none]
# [ (data) | (pointer) (data) | (pointer)]

class linked_list:
    def __init__(self):
        self.head = None
        # [Head -> None] (initializes an empty list)
    
    def insert_at_beginning(self, data):
        node = Node(data)
        # creates [Head--> [(new data)-->] None]
        
        node.next = self.head
        # [[(new data)-->] to [(new data)--> [Head-->] ] ]
        
        self.head = node
        # Old: [Head--> [(anything else)--> [None] ] ] 
        # Inserting: [(new data)--> [Head--> [(anything else)--> [None] ] ] ]
        # New: [Head--> [(new data)--> [(anything else)--> [None] ] ] ]
    
    def insert_at_end(self, data):
        node = Node(data)
        #Checks if empty
        #If it is, sets head to beginning of list
        if self.head is None:
            node.next = self.head
            self.head = node
        #If the list is not empty, goes through each node until the end. Then adds new node.
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            node.next = self.head
            self.head = node
    
    def deleteAtEnd(self):
        cur = self.head
        if self.head is None:
            print("Nothing to delete.")
        else:
            while cur.next.next is not None:
                cur = cur.next
            cur.next = None
    
    def delete_at_beginning(self):
        node = self.head
        if node.next is None:
            self.head = node.next
        else:
            self.head = self.head.next
    
    # Other functions
    def find_node(self, node_data):
        cur_node = self.head
        num = 0
        while cur_node:
            if cur_node.data == node_data:
                return num
            else:
                cur_node = cur_node.next
                num += 1
    
    def find_node_index(self, node_index):
        cur_node = self.head
        num = 1
        try:
            while num != node_index:
                cur_node = cur_node.next
                num += 1
            return cur_node.data
        except IndexError or AttributeError:
            while num != node_index-1:
                cur_node = cur_node.next
                num += 1
            return cur_node.data
    
    # def edit_node(self):
    #     temp = self.head
    #     finder = input("Input node data to edit: ")
    #     num = self.find_node(int(finder))
    #     input_choice = input("Input edited data: ")
    #     # make a change node function
    #     listies = []
    #     while temp:
    #         listies.append(temp.data)
    #         temp = temp.next
    #     temp = self.head
    #     for _ in range(num-1):
    #         temp = temp.next
    #     # maybe insert into list, remake list into linked list
    #     new_node = Node(input_choice)
    #     temp.next = new_node # deletes the rest of the linked list
    #     num1 = 0 + (num - 1)
    #     for _ in range(len(listies) - (num - 1)):
    #         self.insert_at_end(listies[num1])
    #         num1 += 1
    
    def edit(self, node_data, changed_node_data):
        temp = self.head
        num = self.find_node(node_data)

        for _ in range(int(num)):
            temp = temp.next

        new_node = Node(changed_node_data)
        if temp.next is None:
            new_node.next = temp.next
        else:
            new_node.next = temp.next.next
        temp.data = new_node.data
    
    def display(self):
        temp = self.head
        # [Temp(Head)-->[(Data)-->[None]]
        while temp:
            print(temp.data, end=" ")
            
            temp = temp.next
            # [(Head)-->[Temp(data)-->[None]]]
    
    def length(self):
        temp = self.head
        num = 0
        while temp:
            temp = temp.next
            num += 1
        return num
