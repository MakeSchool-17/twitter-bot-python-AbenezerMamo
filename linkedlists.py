from node import *                                   # Have to import


class LinkedList:                               # Class creation
    def __init__(self):                   # Init
        self.head = None                  # Set head

    def insert(self, data):                     # Insert
        new_node = Node(data)                   # Create node with data
        new_node.next_node = self.head          # Move to front
        self.head = new_node                    # JIMMY HATES THIS CODE <32

    def find(self, key):                        # Find
        current = self.head                     # Tracker, start at head
        while current:                          # Check if exists
            if current.data[0] == key:          # Check value
                return current                  # Return the node if found. To acesss, just call current.data[1]
            current = current.next_node         # Keep going
        return None                             # Give up

    def delete(self, key):                                          # Delete
        current = self.head                                         # Set starting point
        if current.data[0] == key:                                  # Check to see if the first Node is the one you want to del
            deleted_node = self.head                                # Remembers the code to be deleted
            self.head = current.next_node                           # This actually deletes it by skipping the Node deleted
            return deleted_node                                     # Returns the deleted node.....you know just in case
        while current:                                              # Check to see if we still have nodes left
            if current.next_node.data[0] == key:                    # Checks to see if it found the key
                deleted_node = current.next_node                    # If it is there, then it just remembers it
                current.next_node = current.next_node.next_node     # This deletes it by skipping the pointer to the deleted node
                return deleted_node                                 # Returns the deleted node
            current = current.next_node                             # If it isn't found then keep going to the next node
        return None                                                 # If it doesn't find it, then it just returns None
