def cached(f):
    fibo_dict = {}

    def memo(n):
        if n in fibo_dict.keys():
            return fibo_dict[n]
        print('Called func')
        res = f(n)
        fibo_dict[n] = res
        return res

    return memo


@cached
def fibonacci(n):
    assert n >= 0

    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i))

for i in range(10):
    print(fibonacci(i))