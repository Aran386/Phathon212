def ceng_letter(m, b, c):
    i = 0
    s = ""
    while i < len(m):
        if m[i] == b:
            s += c
        else:
            s += m[i]
        i += 1
    return s


str1 = "Я изучаю Nython . Мне нарвиться Nython. Nython очень интресный язык программированя"
print("str1 =", str1)
str2 = ceng_letter(str1, 'N', 'P')
print("str2 = ", str2)


def cange_letter2(f, k):
    i = 0
    s = ' '
    while i < len(f):
        if f[i] != k:
            s += f[i]

        i += 1
    return s


a2 = '0123456789'

a21 = list(a2)
# print(a21)
b2 = str(input("Введиет номер позиции от 0 до 9, ->"))
s2 = cange_letter2(a2, b2)
print("s1 =", a2)
print('s2 =', s2)


def cange_letter3(f, k):
    i = 0
    s = ' '
    while i < len(f):
        if f[i] != k:
            s += f[i]

        i += 1
    return s


a3 = '012345363738494'

a31 = list(a3)
# print(a21)
b3 = str(input("Введиет номер позиции от 0 до 9, ->"))
s32 = cange_letter3(a3, b3)
print("s =", a3)
print('s2 =', s32)


def doble(n):
    n_2 = ""
    while n > 0:
        n_2 = str(n % 2) + n_2
        n = n // 2
    return n_2


a4 = int(input("Введите целое число ->"))

print(doble(a4))
