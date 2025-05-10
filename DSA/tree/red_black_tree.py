from collections import deque


def tree_height(root):
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))


def print_rbt(root):
    if root is None:
        print("[empty tree]")
        return

    height = tree_height(root)
    max_width = 2 ** height + 2 ** 6
    q = deque([(root, 0, max_width, 0)])

    prev_level = 0
    line = ''
    while q:
        node, left, right, level = q.popleft()
        if level != prev_level:
            print(line)
            line = ''
            prev_level = level

        mid = (left + right) // 2
        space = mid - len(line)
        line += ' ' * space + f'{'R' if node.red else 'B'}|{node.val if node.val != NIL else 'nil'}'

        if node.left:
            q.append((node.left, left, mid, level + 1))
        if node.right:
            q.append((node.right, mid + 1, right, level + 1))

    print(line)


class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


NIL = object()


class RBTree:
    def __init__(self):
        self.nil = RBNode(NIL)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return

        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent.parent.left == pivot_parent:
            pivot_parent.parent.left = pivot
        elif pivot_parent.parent.right == pivot_parent:
            pivot_parent.parent.right = pivot

        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return

        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent == self.root:
            self.root = pivot
        elif pivot_parent.parent.left == pivot_parent:
            pivot_parent.parent.left = pivot
        elif pivot_parent.parent.right == pivot_parent:
            pivot_parent.parent.right = pivot

        pivot.right = pivot_parent
        pivot_parent.parent = pivot

    def insert(self, val):
        new_node = RBNode(val)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
            self.root.red = False
            return

        assert new_node.val != parent.val, 'should not happen'

        if new_node.val < parent.val:
            parent.left = new_node

        if new_node.val > parent.val:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            parent = new_node.parent
            grandparent = parent.parent
            if grandparent is None:
                break

            if parent == grandparent.right:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if new_node == parent.left:
                        new_node = parent
                        self.rotate_right(new_node)
                        parent = new_node.parent

                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)

            elif parent == grandparent.left:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    new_node = grandparent
                else:
                    if new_node == parent.right:
                        new_node = parent
                        self.rotate_left(new_node)
                        parent = new_node.parent

                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)

        self.root.red = False


def main():
    tree = RBTree()
    for i in [4, 2, 44, 12, 7, 69, 47, 48, -1000, 420, 500009, 8000000, 8, 4]:
        tree.insert(i)
        print(f'AFTER INSERT: {i}')
        print('#' * 20)
        print_rbt(tree.root)


if __name__ == '__main__':
    main()
