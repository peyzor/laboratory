class Foo:
    @property
    def attr1(self):
        print('accessing attr1 to get the value')
        return 69

    @attr1.setter
    def attr1(self, value):
        print('accessing attr1 to set the value')
        raise AttributeError('Cannot change the value')


class Bar:
    def fget(self):
        print('accessing attr1 to get the value')
        return 420

    def fset(self, value):
        print('accessing attr1 to set the value')
        raise AttributeError('Cannot change the value')

    attr1 = property(fget, fset)


if __name__ == '__main__':
    # my_foo_obj = Foo()
    # print(my_foo_obj.attr1)
    # my_foo_obj.attr1 = 10
    # print(my_foo_obj.attr1)

    my_foo_obj = Bar()
    print(my_foo_obj.attr1)
    my_foo_obj.attr1 = 20
    print(my_foo_obj.attr1)
