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

    def add_to_head(self, node):
        if not self.head:
            self.head = node
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
    for item in ll:
        print(item.val)

    print('-' * 20)
    for item in ll:
        print(item.val)

    print('LLQ', '-' * 20)
    llq = LLQueue(n1)
    while llq:
        item = llq.remove_from_head()
        if not item:
            break

        print(item.val)


if __name__ == '__main__':
    main()
