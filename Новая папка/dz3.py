
a = input("Bведите символ: ")
b = int(input("Введите количество символов: "))
slk = int(input("Введите ориентацию символа: 0 - горизонтальная, 1 - вертикальная - "))
if slk == 0:
    print(a*b)
else:
    i = 0
    while i < b+1:
        print(a)
        i += 1





a1 = "-"
b1 = "+"
print(b1*15)
print(a1*15)
print(b1*15)
print(a1*15)
print(b1*15)

a3 = int(input("Введите первое число: "))
b3 = int(input("Введите второе число: "))
c3 = int(input("Введите третье число: "))
d3 = (a3 if a3 > c3 else c3) if a3 > b3 else (b3 if b3 > c3 else c3)
print("Максимальное значение: ", d3)

a4 = float(input("Введите первое число: "))
b4 = float(input("Введите второе число:  "))
c4 = int(input(" Выберите операцию : 1 - унараный минус к операнду, 2 - Сложение, 3 - Вычитание, 4 - Деление, 5 - Умножение, 6 - Деление по модулю, 7- Находит меньшее число, 8- Находит большее число -"))

if b4== 0:
    res = "На ноль делить нельзя!"
elif c4 ==1:
    a4 = -a4
    b4 = -b4
    res = str(a4) + " и " + str(b4)

elif c4 == 2:
    res = a4 + b4
elif c4 == 3:
    res = a4 - b4
elif c4 == 4:
    res = a4/b4
elif c4 == 5:
    res = a4*b4
elif c4 == 6:
    res = a4%b4
elif c4 == 7:
    res = a4 if a4 < b4 else b4
else:
    res = a4 if a4 > b4 else b4
print("Результат действия: " + str(res))


