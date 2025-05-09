from collections import deque


def bst_height(root):
    if root is None:
        return 0
    return 1 + max(bst_height(root.left), bst_height(root.right))


def bst_print(root):
    if root is None:
        print("[empty tree]")
        return

    height = bst_height(root)
    max_width = 2 ** height
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
        line += ' ' * space + str(node.val)

        if node.left:
            q.append((node.left, left, mid, level + 1))
        if node.right:
            q.append((node.right, mid + 1, right, level + 1))

    print(line)


def bst_min(root):
    if root is None:
        return None

    if root.left is None:
        return root.val

    return bst_min(root.left)


def bst_max(root):
    if root is None:
        return None

    if root.right is None:
        return root.val

    return bst_max(root.right)


class BSTNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
                return

            self.left.insert(val)
            return

        else:
            if self.right is None:
                self.right = BSTNode(val)
                return

            self.right.insert(val)
            return

    def delete(self, val):
        if self.val is None:
            return None

        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)

            return self

        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)

            return self

        if not self.right:
            return self.left

        if not self.left:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left is not None:
            min_larger_node = min_larger_node.left

        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self


def main():
    root = BSTNode()
    for i in [4, 2, 44, 12, 7, 69, 47, 48, -1000, 420, 500009, 8000000, 8, 4]:
        root.insert(i)

    print('ORIGINAL', '#' * 35)
    bst_print(root)

    root.delete(-1000)
    root.delete(12)
    root.delete(44)

    print('AFTER DELETE', '#' * 30)
    bst_print(root)

    print('-' * 40)
    print('min', bst_min(root))
    print('max', bst_max(root))


if __name__ == '__main__':
    main()
