class OneDigitNumericValue:
    def __init__(self, name):
        # The descriptor is initialized once per class and is shared between instances of the class

        # If you store values like self.value = 5 then the values is shared for all the instances

        # We can't store values here like self.value = {} like obj: 5 another_obj: 6 because
        # it keeps a strong reference to the obj and prevents the garbage collector from destroying the obj

        # CONCLUSION: DO NOT STORE VALUES IN THE DESCRIPTOR, WE MUST STORE THEM ON THE __dict__ OF THE OBJECT ITSELF

        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value


class Foo:
    # you have to pass the name of the attribute to the descriptor for this to work
    number = OneDigitNumericValue('number')


class OneDigitNumericValue2:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None):
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value


class Bar:
    # because of the __set_name__ we don't have to pass the name here (introduced in python 3.6)
    number = OneDigitNumericValue2()


if __name__ == '__main__':
    my_foo_obj = Foo()
    my_second_foo_obj = Foo()

    my_foo_obj.number = 3
    print(my_foo_obj.number)
    print(my_second_foo_obj.number)

    my_third_foo_obj = Foo()
    print(my_third_foo_obj.number)

    my_bar_obj = Bar()
    my_second_bar_obj = Bar()

    my_bar_obj.number = 3
    print(my_bar_obj.number)
    print(my_second_bar_obj.number)

    my_third_bar_obj = Bar()
    print(my_third_bar_obj.number)
