class Node:
    def __init__(self, data):
        self.item = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_in_emptylist(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return

        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def insert_after_item(self, x, data):
        if self.head is None:
            print('empty list')
            return
        else:
            n = self.head
            while n is not Node:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print('item not in the list')
            else:
                new_node = Node(data)
                new_node.prev = n
                new_node.next = n.next
