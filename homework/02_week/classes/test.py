def memoize(func):
    # func.cache = {}
    func.cache = {}
    print ('Entering')

    def wrapper(n):
        if n not in func.cache:
            func.cache[n] = func(n)

        print (func.__name__, n, func.cache)
        return func.cache[n]

    return wrapper


@memoize
def fibonacci1(n):
    assert n >= 0

    if n < 2:
        return n

    return fibonacci1(n - 1) + fibonacci1(n - 2)

@memoize
def fibonacci2(n):
    assert n >= 0

    if n < 2:
        return n

    return fibonacci2(n - 1) + fibonacci2(n - 2)


def adder(to_add):
    def add(x):
        return x + to_add

    return add


fibonacci1(12)
fibonacci2(12)
