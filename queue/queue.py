"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_end(value)
        # self.storage.insert(0,value)
        # self.size = len(self.storage)

    def dequeue(self):
        if self.size == 0:
            return None
        else: 
            self.size -= 1
            return self.storage.remove_from_head()
        # if self.size > 0:
        #     value = self.storage.pop()
        #     self.size = len(self.storage) 
        #     return value
        
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

    def add_to_end(self, value):
        # regardless of if the node is empty or not, we need to wrap value in a node
        new_node = Node(value)

        # if queue is empty set new_node as the head
        if not self.head:
            self.head = new_node
        else:
        # start at the head
            current = self.head
            # as long as there is another node
            while current.get_next() is not None:
                # traverse the list to the end
                current = current.get_next()
            # add new_node to the end
            current.set_next(new_node)
        

    def remove_from_head(self):
        # if this is the first item in the queue (first out)
        if self.head:
            # store value to return later
            value = self.head.get_value()
            # set head to the next node
            self.head = self.head.get_next()
            return value
