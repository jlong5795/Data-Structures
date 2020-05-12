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