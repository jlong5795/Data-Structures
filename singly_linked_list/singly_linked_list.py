# from guided project
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

class LinkedList:
    def __init__(self):
        # first node in the list 
        self.head = None
        # last node in the list
        self.tail = None
  
    # we don't have access to the end of the linked list
    # when we want to add to the end, we need to traverse the whole linked list to get to the end
    # O(n) - linear

    # we have direct access to end of the list so we can add nodes to it directly
    def add_to_end(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node 
        new_node = Node(value)
        # what if the list is empty? 
        if not self.head and not self.tail:
            # set both head and tail to new_node
            self.head = new_node
            self.tail = new_node
        # what if the list isn't empty?
        else:
            # set the current tail's next to the new node
            self.tail.set_next(new_node)
            # set self.tail to the new node
            self.tail = new_node

    # we already have access so no traversal needed
    # # O(1)       
    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head 
            value = self.head.get_value()
            # remove the value at the head 
            # update self.head 
            self.head = self.head.get_next()
            return value

    def add_to_head(self, value):
        # wrap in node
        new_node = Node(value)
        # is list empty?
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # if list isn't empty
        else:
            new_node.set_next(self.head)
            self.head = new_node