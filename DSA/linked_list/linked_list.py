class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_to_tail(self, node):
        if not self.head:
            self.head = node
            return

        head = self.head
        while head.next:
            head = head.next

        head.next = node

    # # generator impl
    # def __iter__(self):
    #     head = self.head
    #     while head:
    #         yield head
    #         head = head.next

    # classic impl
    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        curr = self.current
        if not curr:
            raise StopIteration('hold up')

        self.current = curr.next
        return curr


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node


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
    n3 = Node(4)
    ll.add_to_tail(n3)
    for item in ll:
        print(item.val)


if __name__ == '__main__':
    main()
