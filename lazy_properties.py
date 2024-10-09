import time


# slow properties
class DeepThough:
    def meaning_of_life(self):
        time.sleep(3)
        return 69


class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, instance, owner):
        instance.__dict__[self.name] = self.function(instance)
        return instance.__dict__[self.name]

    # NOTICE: the lazy property descriptor will not work if the __set__ is defined
    # because with it, it becomes a data descriptor
    # PYTHON LOOKUP CHAIN:
    # 1. DATA DESCRIPTORS
    # 2. __dict__ of the obj (second time onwards the value is retrieved from here)
    # 3. NON-DATA DESCRIPTORS (first time it's called, it misses in step 2 and reaches here, it gets calculated and store in step 2)
    # 4. type(obj).__dict___
    # 5. und so weiter...
    # def __set__(self, instance, value):
    #     raise AttributeError('something')


class DeepThough2:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 69


if __name__ == '__main__':
    # dp = DeepThough()
    # print(dp.meaning_of_life())
    # print(dp.meaning_of_life())
    # print(dp.meaning_of_life())

    dp = DeepThough2()
    print(dp.meaning_of_life)
    print(dp.meaning_of_life)
    print(dp.meaning_of_life)
