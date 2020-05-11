"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack: # implemented using a list (array)
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)

#     def pop(self):
#         if self.size > 0:
#             value = self.storage.pop()
#             self.size = len(self.storage)
#             return value

class Node:
    def __init__(self, value=None, next_node=None):
        # value at this node
        self.value = value
        # reference to the next node in the list of nodes
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next reference to the passed in node
        self.next_node = new_next

class LinkedList: # implemented with linked list
    def __init__(self):
        # first node in the list (calling head as in head vs tail)
        self.head = None

    def add(self, value):
        # regardless of if the node is empty or not, we need to wrap value in a node
        new_node = Node(value)

        # set next reference to current head
        new_node.next_node = self.head 

        # becomes new head
        self.head = new_node 

    def remove(self):
        # if the list is empty
        if not self.head:
            return None
        # if the list is NOT empty
        else:
            # value set to current head
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def push(self, value):
        self.storage.add(value)
        self.size = self.size + 1

    def pop(self):
        if self.size > 0:
            self.size = self.size - 1
            return self.storage.remove()

    def __len__(self):
        return self.size
