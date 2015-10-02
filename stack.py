class Stack:

    def __init__(self):
        self.head = None
        self.size = 0


    def push(self):
        new_node = Node()
        new_node.data = data
        next_node = self.head
        self.head = new_node
        self.head.next = next_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            first_element = self.head
            self.head = first_element.next
            self.size -= 1
            return first_element.data

    def peek(self):
        if self.is_empty: # If this exists. You can also check if self.head actually exists
            return None
        else:
            return self.head.data

    def size(self):
        return self.size

    def __str__(self):
        return_str = ''
        current_node = self.head
        while current_node is not None:
            return_str += str(current_node.data)
            current_node = current_node.next
        return return_str

    def is_empty(self):
        return self.head is None

class Node:
    def __init__(self):
        pass
