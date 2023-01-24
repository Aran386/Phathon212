def func_decorator(func):
    global d

    def wrappe(z):
        print("code befor")
        func(z)
        v = sum(d) / len(d)
        print("Среднеt арифмитическое ", v)

    return wrappe


@func_decorator
def func_base(x):
    a = sum(x)
    print('Сумма чисел ->', a )
    b = a / len(x)
    print(round(b))


d = (2, 3, 4, 100)
func_base(d)


def decor(func):
    def wrap(*args):
        print("Среднее арифметическое чисел", *args, "=", func(*args) / len(args))

    return wrap


@decor
def summ(*args):
    print("Сумма чисел", *args, "=", sum(args))
    return sum(args)


summ(2, 3, 3, 4)
