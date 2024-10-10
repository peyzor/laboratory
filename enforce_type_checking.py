import functools
import inspect


def enforce_type_checking(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        signature = inspect.signature(func)
        parameters = signature.parameters

        # args
        for i, arg in enumerate(args):
            param_name = list(parameters.keys())[i]
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument {param_name} must be of type '{param_type.__name__}'")

        # kwargs
        for param_name, arg in kwargs.items():
            param_type = parameters[param_name].annotation
            if not isinstance(arg, param_type):
                raise TypeError(f"Argument {param_name} must be of type '{param_type.__name__}'")

        return func(*args, **kwargs)

    return wrapper


@enforce_type_checking
def multiply_numbers(x: int, y: int) -> int:
    return x * y


if __name__ == '__main__':
    result = multiply_numbers(5, 7)
    print("Result:", result)

    result = multiply_numbers("5", 7)
