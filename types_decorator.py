import functools

"""Type checker for functions

Implement a types decorator for function arguments validation.
The decorator must match number of arguments to the number of
types, each argument's type to the corresponding type, provided
in the decorator. The type of returning value must be validated
as well. It must be provided to the decorator by _ret keyword
argument. If any mismatch occurs the decorator must raise 
Exception.
Resulted decorator must work with any Python function."""


def types(*args, _ret=None):
    def _types(func: callable):
        @functools.wraps(func)
        def wrapper(*fargs):  # function arguments
            f_list = args
            my_list = fargs
            res = func(*fargs)
            if len(my_list) != len(f_list):
                raise ValueError("Number of arguments do not match"
                                 " to the number of types")

            for idx, arg in enumerate(my_list):
                if not (isinstance(arg, (f_list[idx])) and
                        isinstance(res, _ret)):
                    raise TypeError('Occurred type mismatch')
                return res

        return wrapper

    return _types


@types(int, float, _ret=float)
def plus(a, b):
    return a + b


@types(str, _ret=str)
def rev(txt):
    return txt[::-1]


if __name__ == '__main__':
   # x = rev("բարև")
    y = plus(1, 3.0)
    print(y)
