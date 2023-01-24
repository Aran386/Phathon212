a = tuple(input('=>'))
# a = (2, 5, 3, 5, 2, 3, 6, 5, 1)
print(a)
b = []
for i in a:
    if i not in b:
        b.append(i)
        print("Количество ", i, '=', a.count(i))


def change_kort(lst):
    lst_1 = []
    lst_2 = []
    for i in lst:
        if i not in lst_1:
            lst_1.append(i)

    df = len(lst_1)
    for i in range(1, df + 1):
        lst_2.insert(i, lst_1[df - i])
    cr = tuple(lst_2)

    return print(cr)


a = [1, 2, 3, 2]
b = [2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]
print(a)
change_kort(a)
print(b)
change_kort(b)

a3 = ('ab', 'abcd', 'cde', 'adc', 'def')
print(a3)
s = 'ab'
if s in a3:
    print("S = ", s)
    print("Yes")
