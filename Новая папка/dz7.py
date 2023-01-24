import math


def pram(st1, st2):
    return st1 * st2


def treg(str3, st4):
    return 0.5 * str3 * st4


def circ(st5):
    return math.pi * st5 ** 2


num = int(input("Выбирете площадь какой фигуры нужно найти: 1 - прямоугольник, 2- треугольник, 3 - круг: =>"))
if num == 1:
    a = float(input(("Введите 1 сторону прямоугольника =>")))
    b = float(input("Введите 2 строну прямоугольника =>"))
    res = pram(a, b)
elif num == 2:
    a = float(input(("Введите основание  треугольника =>")))
    b = float(input("Введите высоту  треугольника =>"))
    res = treg(a, b)
elif num == 3:
    a = float(input(("Введите радиус окружности =>")))
    res = circ(a)
else:
    print("Нет такой фигуры, к сожалению. Попробуйте еще раз.")
    exit()

print("Площадь фигуры :", round(res, 3))
