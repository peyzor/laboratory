import time


class LazyAttribute:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, instance, owner):
        instance.__dict__[self.name] = self.function(instance)
        return instance.__dict__[self.name]


class DeepThought:
    @LazyAttribute
    def meaning_of_life(self):
        time.sleep(3)
        return 42


def main():
    class OneDigitNumericValue:
        def __init__(self):
            self.value = 0

        def __get__(self, obj, type=None) -> object:
            return 42

        # def __set__(self, obj, value) -> None:
        #     if value > 9 or value < 0 or int(value) != value:
        #         raise AttributeError("The value is invalid")
        #     self.value = value

    class Foo:
        number = OneDigitNumericValue()

        def __init__(self):
            self.number = 5

    my_foo_object = Foo()
    my_second_foo_object = Foo()

    # my_foo_object.number = 3
    print(my_foo_object.number)
    print(my_second_foo_object.number)


if __name__ == '__main__':
    import time


    class LazyProperty:
        def __init__(self, function):
            self.function = function
            self.name = function.__name__

        def __get__(self, obj, type=None) -> object:
            obj.__dict__[self.name] = self.function(obj)
            return obj.__dict__[self.name]

        def __set__(self, instance, value):
            pass


    class DeepThought:
        @LazyProperty
        def meaning_of_life(self):
            time.sleep(3)
            return 42


    my_deep_thought_instance = DeepThought()
    print(my_deep_thought_instance.meaning_of_life)
    print(my_deep_thought_instance.meaning_of_life)
    print(my_deep_thought_instance.meaning_of_life)
