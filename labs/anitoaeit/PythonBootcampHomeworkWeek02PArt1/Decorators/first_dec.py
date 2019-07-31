def logged(f):
    def wrapped_func(*args, **kwargs):
        print('You called the function with ({}, {})'.format(args, kwargs))
        res = f(args, kwargs)
        print('It returned {}'.format(res))
        return res
    return wrapped_func


@logged
def func(*args, **kwargs):
    return 3 + len(args[0])


print(func(1, 2, 3, 4, key = True))
