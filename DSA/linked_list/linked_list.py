class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __str__(self):
        return f'{self.val}'


class LinkedList:
    def __init__(self, head):
        self.head = head
        # if keeping track of tail is necessary
        self.tail = None

    def add_to_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head = node

    def add_to_tail(self, node):
        if not self.head:
            self.head = node
            return

        head = self.head
        while head.next:
            head = head.next

        head.next = node
        self.tail = node

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        curr = self.current
        if not curr:
            raise StopIteration('hold up')

        self.current = curr.next
        return curr


class LLQueue:
    def __init__(self, head):
        self.head = head
        self.tail = None

    def remove_from_head(self):
        if not self.head:
            return None

        prev_head = self.head
        self.head = prev_head.next
        if not self.head:
            self.tail = None

        return prev_head

    def add_to_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head = node

    def add_to_tail(self, node):
        if not self.head:
            self.head = node
            return

        head = self.head
        while head.next:
            head = head.next

        head.next = node
        self.tail = node

    def __iter__(self):
        head = self.head
        while head:
            yield head
            head = head.next

    def __str__(self):
        return f'{self.val}'


def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.set_next(n2)
    n2.set_next(n3)

    ll = LinkedList(n1)
    for item in ll:
        print(item.val)

    print('-' * 20)
    n4 = Node(4)
    ll.add_to_tail(n4)
    print('TAIL: ', ll.tail)
    for item in ll:
        print(item.val)

    print('-' * 20)
    n5 = Node(5)
    ll.add_to_head(n5)
    print('TAIL: ', ll.tail)
    for item in ll:
        print(item.val)

    print('LLQ', '-' * 20)
    n6 = Node(6)
    llq = LLQueue(n1)
    llq.add_to_tail(n6)
    while llq:
        item = llq.remove_from_head()
        print(item.val)


if __name__ == '__main__':
    main()
