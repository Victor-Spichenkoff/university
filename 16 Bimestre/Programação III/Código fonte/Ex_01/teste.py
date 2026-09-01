class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to the next node, initially None


class LinkedList:
    """Represents the linked list structure."""
    def __init__(self):
        self.head = None  # The list starts empty

    def insert_at_end(self, data):
        """Inserts a new node with the given data at the tail of the list."""
        new_node = Node(data)

        # Case 1: If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return

        # Case 2: Traverse to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # Change the next pointer of the last node to the new node
        current.next = new_node

    def display(self):
        """Helper method to print the linked list elements."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")


# --- Demonstration ---
if __name__ == "__main__":
    ll = LinkedList()
    
    # Insert elements at the end
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)

    # Print the resulting list
    ll.display()  # Output: 10 -> 20 -> 30 -> None