# print('Hello word !')
# name = 'elena'
# print(('Hello', name))
# age = 20
# a = f = d = n = 1
# print(a, f, d)
# a, b, c = 'Hello', 5, False
# print(a, b, c)
#
# print(6 - 5)
# print(6 + 5)
# print(6 / 5)
# print(6 // 5)
# print(6 ** 2)
# print(7 % 2)
# a, b, c = 5, 7, 3
# summ = a + b + c
# sre_parse = summ / 3
# print(a + b + c)
# print(a * b * c)
# print((a + d + c) / 3, sre_parse)
# num = 10
# num +=5
# print(num)
# a1 = "hello"
# print(a1, type(a1))
# a1 = 5
# print(a1, type(a1))
# name1 = 'Jaki'
# age1 = 30
# print("My name is " + name1)
# print("My name is " + name1 + "  I am " + str(age1) + ' yaer old')
# a = 1
# b = 2
# print('a ;', a)
# print('b:', b)
# a, b = b, a
# print('a ;', a)
# print('b:', b)
# print('строка символа строка символа строка символа строка символа строка символа строка символа строка символа строка'
#       ' символастрока символа')
# print('Докмент \" file.py\"')
# # Функция преобразования типов - функция явного преобразования
# print(int(3.8))
# a2 = 3.8
# print(type(round(a2)))
# # float

# a = 1
# b = 2
# print("a : ", a)
# print()
# print("b : ",b)
# print("b : ",b, "\n b:",b)
# name = "Виктор"
# age = 28
# print("Меня зововут", name, "I", age, "yaer old")
# print("Меня зововут", name, "I", age, "yaer old", sep = " $", end=" ")
# print("Меня зововут " + name +  "I am " + str(age) +  " yaer old", end=" " )
# print("I am learning Python.")
# name = input("Input name: ")
# print("Hellj", name)
# num =int( input("input chislo "))
# power = int(input("input stepenm "))
# res = num**power
# print('chislo ', num, 'v stepeny' , power, 'ravno', res)

# a1 = int(input("Введите число 1 : "))
# a2 = int(input("Введите число 2: "))
# a3 = int(input("Введите число 3: "))
# a4 = int(input("Введите число 4: "))
# num_a = (a1 + a2)/(a3 + a4)
# print(round(num_a,2))

# b1 = True
# b2 = False
# print(b1 +5)
# print(b2 +5)
# print(bool("pyton"))
# print(bool(""))
# print(bool(5))
# print(bool(-5))
# print(bool(False))
# print(bool(None))
# test1 = None
# print(test1)

#
#
#
# age = int(input("Input yoar age: "))
# if age >= 18:
#       print("Come in  ")
# else:
#       print("input is inposoble ")
a = 15
b = 15

# st1 = int(input("Введите первую сторону: "))
# st2 = int(input("Введите вторую сторону: "))
# st3 = int(input("Введите третью сторону: "))
# if st1==st2 and st1 == st3 :
#             print("Треугольник равностороний")
# elif st1 == st2 or st2 == st3 or st1 == st3:
#       print("Треугольник равнобедренный")
# else:
#       print("Треугольник разностроронний")

# day = int(input("Введите день недели (цифрой)"))
# if (day >= 1) and day <= 5:
#       print ("Day work")
#       if day == 1:
#             print("monday")
#       if day == 2:
#             print("vtornik")
#       if day == 3:
#             print("sreda")
#       if day==4:
#              print("shetverg")
#       if day == 5 :
#            print("patnisa")
# elif day == 6 or day ==7:
#       print ("The day off")
# else:
#       print (" Такого дня нет")
# if 1 <= day <= 5:
#       print("Прикол")

# dd = int(input("Введите номер месяца : "))
# if 1 <= dd <= 12:
#       if 1<= dd <= 3:
#             print("Winter")
#       if 4<= dd <= 6:
#             print("Spring")
#       if 7 <= dd <= 9:
#             print("Summer")
#       if 10 <= dd <= 12:
#             print("Autom")
# else:
#       print("Нет такого месяца")
# n = 125
# n2 = n%10
# print(n2, n)
# a, b = 30, 30
# minim = "a==b" if a==b else "a>b" if a > b else "b > a"
# print(minim)
# Ternalnoe virogenie
# a, b = 10, 0
# c = a/b if b!=0 else "На ноль делить нельзя"
# print(c)
# Исключения
# try:
#     n = int(input('Введите целое число'))
#     print((n*2))
# except ValueError:
#     print(("Что то пошло не так"))
# try:
#     n = int(input('Введите делимое'))
#     m = int(input('Введите делитель'))
#     print((n/m))
# except ValueError:
#     print(("Что то пошло не так"))
# except ZeroDivisionError:
#     print(("Что то пошло не так"))
# t
# n = input('Введите первое число')
# n1 = input('Введите второе число')
# try:
#     n = int(n)
#     n1 = int(n1)
# except ValueError:
#     # print("n + m")
#    # pass
#    n =str(n)
# finally:
#     print(n+n1)
# Cilkk
#  While
# i = 10
# while i > 0:
#     print("i = ", i)
#     # i = i +1
#     i-=1
# j = 2
# while j < 21:
#     print(j)
#     j+=2
# n = input("Укажите количество символов:")
# i = 0
# while i < 1:
#     print("*", end="")
#     i+=1
# n = input("Введите целое чило:")

# while type(n)!= int:
#     try:
#         n= int(n)
#     except ValueError:
#         print("Число не целое")
#         n =input("Введите целое число")
# if n%2 == 0:
#     print("Четное число")
# else:
#     print("Не четное число")
# i = 0
# while i< 6:
#     print(i,end="")
#     if i==5:
#       # break
#       #   i=i+1
#       # continue
#     i= i +1
# print("\n Цикл завершен")
i = 0
# while True:
#     print(i)
#     if i==5:
#         break
#     i+=1
# while True:
#     n = int(input("Введите положительное число:"))
#     if n<0:
#         break
# print(" Цикл закончен")
# while True:
#     i = 1
#     n = int(input("Введите число"))
#
#     if n == 0:
#         break
#       i=i*n
#
# print(n)

# i = 0
# while i < 10
#     if==5:
#         break
#     print(i)
#     i=i+1
# else:
#     print("Цикл окончен", i)

# kol = int(input("Введите количество чисел последовательности: "))
# i = 1
# ch = float(input('введите число'))
# min_ch = ch
# max_ch = ch
# sum_ch = ch
# while i <kol:
#     ch = float(input("Введите число"))
#     sum_ch+=ch
#     if ch < min_ch:
#         min_ch = ch
#     if ch > max_ch:
#         max_ch = ch
#     i+=1
# print("Количество чисел: ", kol)
# print("Минимальное число", min_ch)
# print("Максимальное число", max_ch)
# print("Среднеарифметическая сумма чисел", sum_ch/kol)

# i = 1
# while i < 5:
#     print("Внешний цикл i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутрений цикл: j = 1", j)
#         j+=1
#     i+=1
# i = 1
# while i < 10:

#     j = 1
#     while j < 10:
#         print(str(i) +  "*" + str(j) + "=" + str(i*j),'\t\t')
#         j+=1
#     i+=1
#
# Цикл for
# for element in  collections:
#     тело цикла
# for i in "Hello":
#     print(i)
# for color in "red", 'yellow', 'grenn', 1 , 20, 20.3:
#     print("color: ",color
# print(range())
# for i in range(0, 10, 2):
#     print(i, end=" ")
# print()
#
# j=0
# while j< 10:
#     print(j, end=" ")
#     j+=2
# print()
# for i in range(20, 10, -2):
#     print(i, end=" ")
# print()
# s=20
# while s > 0:
#     print(s, end=" ")
#     s-=2
#
# a = int(input('введите целое число:'))
# for i in range(1, a + 1):
#     if a%i == 0:
#         print(i, end=" ")
# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
#
# for i in range(3):
#       if i== 1:
#           break
#       print(i)
#
# else:
#     print('done')
#
# w = int(input("введите длинну треугольник "))
# h = int (input("введите высоту прямоугольника"))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h-1 or j==0 or j == w-1:
#            print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# letter = [i for i in 'Hello']
# print(letter)
# num = [i for i in range(30) if i%2 ==0]
# print(num)
# Списки
# nums = [8,3,4,9]
# print(id(nums))
# print(nums[3])
# print(nums[0])
# print(nums[-1])
# nums[1]=256
# print(id(nums[1]))
# nums[1]+=100
# print(id(nums))
# print("длинна списка: ", len(nums))
# s = [1,3,5]
# print(s)
# s1 = list()
# print(s1)
# s2 = list('Hello')
#
# print(s2)
# n = s*6
# print(n)
# n1 = list(range(2,10,2))
# print(n1)
# n = 5
# a = [ i**2 for i in range(1, n+1)]
# print(a)
# c = [i*3 for i in 'list']
# print(c)
# a = [1,2,3]
# b = [4,5]
# c = a +b
# print(c)
# d = c*3
# print(d)
# a = [0]* int(input("введие количество элементов списка: "))
#
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('->'))
# print (a)
#
# a = [int(input("->")) for i in range(int(input("Введите количесвто элементов списка:")))]
# print(a)
# a = [8,4,2,9]
# for i in range(len(a)): индекс
#     print(i)
#     print(a[i], end=" ")
# for elem in a: число
#     print(elem, end=" ")
#
# a = [int(input("->")) for i in range(int(input("Введите количесвто элементов списка N :")))]
# res = 0
# res_1 = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         res+=a[i]
# print("Сумма отрицательных элеметов: ", res)
# for i in a:
#     if i < 0:
#         res_1 +=i
# print("Сумма отрицательных элеметов: ", res_1)
#
# n1 = list(range(21, 40))
# print(n1)
# ch = 0
# sd = 0
# for i in n1:
#     if i% 2 == 0:
#        ch+=1
#     else:
#       sd += i
# print("Количество четных элеметов :", ch)
# print('Сумма не четных элементов :', sd)
#
# a = [int(input("->")) for i in range(int(input("Введите количесвто элементов списка N :")))]
# print(a)
# for i in range (1, len(a)):
#     if a[i] > a[i-1]:
#         print(a[i], end=" ")
# a = [7,8,9,10,12]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)
# a2 = list('Hello word')
# print(a2)
#
# a3 = list(range(2,18,2))
# print(a3)
# a4 = [i*3 for i in 'list']
# a5 = [i for i in range(5,10)]
# print(a4)
# print(a5)
# Срез списка синтаксис список[start: stop: step]
# a = [7,8,9,10,12,25,68]
# print(a[1:5])
# print(a[1::2])
# print(a[::2])
# print(a[::-1])
# print(a[-2:2:-1])
# print(a[-2:1:-1])
# print(a[:-2])
# print(a[10:-2])
# print(a[10:20])
# a = [1,2,3,4,5,6,7]
# b = list(range(1,7+1))
# d = [i for i in range(1, 7+1)]
# print(a)
# print(b)
# print(d)
# print('Print a=>',a[:])
# print('Print a=>',a[1::2])
# print('Print b=>',b[::-1])
# print('Print b=>',b[:1])
# print('Print c=>', d[::2])
# print('Print c=>', d[-1:])
# print('Print c=>', d[3:4])
# print('Print c=>', d[-4:-3])
# print('Print c=>', d[4:])
# print('Print c=>', d[-3:-6:-1])
# print('Print c=>', d[2:5:1])
# a[3:5] =[0,0,0,0]
# print(a)
# a[3:4] = [20]
# print(a)
# a[4] = 50
# print(a)
# a[5] = [60]
# print(a)
# del a[4]
# print(a)
# del a[2:4]
# print(a)
# del a[:]
# print(a)
#
# Методы списка
# print(dir(list))
# s = [7,8,25,36,89,58, 24]
# print(s)
# s1 = list([5,6,8,9])
# s.append(99)
# print("s1 =>",s1)
# print("s =>",s)
# s.extend([33,34,35])
# print("s =>",s)
# s.extend("sorty")
# print("s =>",s)
# s.extend(['didi','lulu'])
# print("s =>",s)
# s.insert(0,-15)
# print("s =>",s)
# s.insert(3,-15)
# print("s =>",s)
#
# a = []
# n = int(input("Введите число значений N :"))
# for i in range(n):
#     r = input("=>")
#     a.append(r)
# print("a =>", a)
# a1 = []
# n1 = int(input("Введите число значений N :"))
# for i in range(n1):
#
#     a1.append(input("=>"))
# print("a1 =>", a1)
# a2 = []
# [ a2.append(int(input("=>"))) for i in range(int(input('Введите число n: ')))]
# print("a2 =>", a2)
#
# data = [int(input("Введите число кратное 3=>")) for i in range(int(input("Введите количество чисел N: ")))]
# data=[]
# n = int(input("Введите количество чисел N: "))
# for i in range(1, n+1):
#     s = int(input('Введите число кратное 3 =>'))
#     if s%3 == 0:
#         data.append(s)
#     else:
#         print(s, "не делеться на 3 без остатка")
# print("data =>", data)
# ata=[]
# n = int(input("Введите количество чисел N: "))
# for i in range(1, n+1):
#     s = int(input('Введите число кратное 3 =>'))
#     ata.append(s) if s%3 == 0 else  print(s, "не делеться на 3 без остатка")
#
#
# print("data =>", ata)

# a =[5,9,2,1,4,6, 4]
# b = [5,2,4,6,8,25]
# d = []
# for i in a:
#     # print("a =>",i, end="" )
#     for j in b:
#         # if i in d:
#         #     continue
#         # print("b=>", j, end='')
#         if i == j :
#          d.append(i)
# print("d =>", d)
# a = [1,2,3]
# b = [11,22,33]
# c = []
# print("a =>",a)
# print('b =>', b)
# # if len(a)>len(b):
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# # for i in range(len(a),len(b)): для большего списка
# #     c.append(b[i])
# print("c =>", c)
# a = [1,2,3,4,2,5,6]
# a.remove(3)
# print(a)
# a.remove(2)
# print(a)
# last = a.pop() #удаляет последний элемент из списка и возварщает удаленное значениу
# print(a, last)
# last1 = a.pop(1)
# print(a, last1)
# a.clear()
# print(a)
# print("Введите элементы списка")
# a = []
# [ a.append(int(input("=>"))) for i in range(int(input('Введите элементы списка n : ')))]
# c = int(input("Введите индекс k : 0 <= k <= n   "))
# print(a)
# a.pop(c)
# print(a)
# s = 0
# a = [5,9,10]
# for i in a:
#     s+=i
# print(s)
# a = [5,9,6,9,8,7,8,9]
# print(a)
# num = a.count(9)
# num2 = a.count(8)
# print(num, num2)
# int = a.index(9,3,-1)
# print(int)b

# a= [5,9,7]
# b = a
# c = a.copy()
# b.append(120)
# print( "a =>", a)
# print("b =>", b)
# print(id(a))
# print(id(b))
# print(id(c))
# a.reverse()
# print(a)
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

# s = ['Виталий'," Исмуил",'Инокентий '," АФина"]
# print(s)
# s.sort()
# print(s)
# s.sort(key=len, reverse=True)
# print(s)
# b = sorted(s)
# print("b ",b)
# print("s " ,s)

# Генерация случайных данных
# import random
# print(random.random())
# print(random.randint(0, 9)) #jn 1 from 9 bkl
# print(random.randrange(9)) #no 9 brl
# print(random.randrange(0, 10, 2))
# from random import randint
# from random import *


# print(r.randint(1, 9))
# print(r.uniform(10.5, 25.3))
# city = ['Москва','Новосибирск','Воронеж','Сочи','Екатеренбург']
# print(r.choice(city))
# print(r.choices(city,k=3))
# r.shuffle(city)

import random
# mas = [input() for i in range(10)]
# mas1 = [random.randint(50, 100) for i in range(10)]
# print(mas1)
# lst = [4,6, 8 ,9 ,1]
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# stp = random.randint(10, 100)
# print(stp)
# str1 = [random.randint(10, 100) for i in range(11)]
# print(str1)
# b = max(str1)
# str1.remove(b)
# str1.insert(0, b)
# print(max(str1))
# d = [3, 20, 17, -13, 8, -14,3, -8, -16, 5]
# d.sort(reverse=True)
# print(d)
# d1 = [random.randint(-20,20) for i in range(10)]
# d1.sort(reverse=True)
# print(d1)
# d2 = [random.randint(0,100) for i in range(30)]
# print(d2)
# print("Min =>", min(d2))
# print("Index min :", d2.index(min(d2)))
# # inmin = d2.index(min(d2))
# d2min = d2[d2.index(min(d2)):] #альтарнитивный вариант
# del d2[0:d2.index(min(d2))]
# print(d2)
# print(d2min)

# x = list("1a2b3c4d")
# print(x)
# print('a' in x)
# print('a'not in x)
# print('m' in x)
# print('m' not in x)
# lid = [ ]
# if len(lid) ==0:
#     print("Список пустой")
# if not lid:
#     print("Список пустой")


# a5 = []
# a6= []
# n1 = int(input("Введите размер первого списка :"))
# n2 = int(input("Введите размер второго списка: "))
# a1 =[random.randint(0,100) for i in range(n1)]
# a2 = [random.randint(0,100) for i in range(n2)]
# # [a1.append(int(input("=>"))) for _ in range(int(input('Введите размер первого спиcка: ')))]
# print("Список первый: ",a1)
# # [ a2.append(int(input("=>"))) for i in range(int(input('Введите размер второго  спиcка: ')))]
# print("Список второй: ",a2)
# a3 = a1 + a2
#
# print("Третий список ", a3)
# a4 = [max(a1), max(a2)]
# print('a4 =>',a4)
# for i in a1:
#     for j in a2:
#         if i == j:
#             a5.append(j)
#
# for i in range(len(a1)):
#     if a1[i] not in a5:
#         a6.append(a1[i])
# for i in range(len(a2)):
#     if a2[i] not in a5:
#         a6.append(a2[i])
# print("Список содержащий элементы из 2 списков без повторений : a6", a6)
# print("Список содержащий элементы из 2 списков повторяющиеся : a5", a5)

# m =[
#     [1, 2 ,3 , 4],
#     [5,6 , 7],
#     [9,10,11,12]
# ]
# print(m)
# print(len(m))
# print(m[1])
# print(m[1][1])
# for sur in range(len(m)):
#    # print("sur =>", m[sur])
#     for pur in range(len(m[sur])):
#         print( m[sur][pur], end=" ")
#     print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# for row2 in m:
#     for x2 in row2:
#         print(x2**2, end='\t\t')
#     print()
# w, h = 10, 10
# matrich = [[x*y for x in range(1,w)]for y in range (1, h)]
# for ml in matrich:
#     for z in ml:
#         print(z,end="\t\t")
#     print()
#
# for x, y in [[1, 2], [3,4], [5,6]]:
#     print(x, '+',  y, '=', x+y)
# for x,y,z in [[1,2,3],[11,12,13],[21,22,23]] :
#     print(x,"+",y,"-",z,"=", x+y-z)
# n = int(input(' введите размернсоть мастрицы:'))
# mas = []
# for i in range(n):
#     mas.append([])
#     for j in range(n):
#         mas[i].append(random.randint(1,100))
# print(mas)
# for row in mas:
#     for x in row:
#         print(x, end="\t")
#     print()
# m = 100
# lst = []
# for k in range(n):
#     if m > mas[k][k]:
#         lst.append(mas[k][k])
#         print(mas[k][k], end="\t ")
#     print()

import math
# num = math.ceil(3.2)
# num2 = math.floor(3.8)
# num3 = math.sqrt(2)
# print(num)
# print(num2)
# print(num3)
# print(math.pi)
# r = int(input('=>'))
# l = 2*r*math.pi
# print(round(l, 2))
import time


# second = time.time()
# print(second)
# locale_time = time.ctime(85864)
# print(locale_time)
# res = time.localtime()
# print(res)
# print(res.tm_year, res.tm_mon, res.tm_zone)
# print(time.strftime("Today is %B %d, %Y"))
# paus =10
# print("Запуска программы", )
# time.sleep(paus)
# print("Pause", paus)
# text = input("Название напоминания")
# local_time = float(input('Через сколько минут:'))
# local_time = local_time*60
# time.sleep(local_time)
# print(text)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)
# import locale
#
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime("Сегодня %B %d, %Y"))

# Function
# a = 20
#
#
# def hello(name, age):
#     print("Hello word", name, "I am ", age, sep=" ")
#
#
# hello('Ira', 20)
# hello("Vacz", 48)
# def get_summ(a, b):
#     print(a + b)
#
#
# get_summ(2, 5)
#
# c = 8
# d = 8
# get_summ(c,d)
# get_summ('sss', 'dddd')
# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2:
#             print(a, end='')
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'X', 'O')
# def get_sum(a, b):
#     print(a, b)
#     if b == 0:
#         return "Делить на ноль нельзя"
#     return a/b
#
#
# ch = get_sum(2, 5)
# print(ch ** 2)


# def change(lst):
#     #lst[0], lst[-1] = lst[-1], lst[0]
#     m = lst.pop()
#     n = lst.pop(0)
#     lst.insert(0, m)
#     lst.append(n)
#     return lst
# print(change([1, 2, 3]))
# print(change([3,9,10,12,18]))
# print(change(['c','b','d']))

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 10 + 1):
#     print(i, 'в кубе =', cube(i))

# def ceck_password(password):
#     has_apper = False
#     has_loew = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_apper = True
#         if "a" <= ch <= "z":
#             has_loew = True
#         if "0" <= ch <= "9":
#             has_num = True
#     if len(password) >= 8 and has_apper and has_loew and has_num:
#         return True
#     else:
#         False
#
#
# p = input("Введите пароль =>")
# if ceck_password(p):
#     print("Это надежный пароль:")
# else:
#     print("Это не надежный пароль!")
# def get_summ(a,b,c=1,d=1):
#     return  a+b+c+d
# print(get_summ(1,23,4,5))
# print(get_summ(2,6))
# print(get_summ(2, 6, d=10))
# def set_param(c=20,s="-"):
#     print(s*c)
# set_param(20,"-")
# set_param(15, "+")
# set_param(5, "*")


# def displyy_info(name, age):
#     print("Name", name, "\nAge", age)
# displyy_info("Ira", 23)
# displyy_info(age=23, name="ira")
# lt1 = [1,2,3]
# lt2 = [1,2,3]
# print(id(lt1))
# print(id(lt2))
#
# print(lt1==lt2)
# print(lt1 is lt2)
# a = "Hello"
# b = "Hello"
# print(id(a))
# print(id(b)
#       )
# print(a==b)
# print(a is b)

# s = "hello"
# print(s, id(s))
# s+='word'
# print(s, id(s))
# s = s + "Word"
# print(s, id(s))
# a = 5
# print(a, id(a))
# a+=1
# print(a, id(a))
# s = "Hello"
# print(s, id(s))
# s += s[1:-1]
# print(s, id(s))
# def add_number(n):
#     print("Внутри функции:", n, id(n))
#     n+=1
#     print("Изменные значения", n, id(n))
#     return n
#
# x= 1
# print("До функции:", x, id(x))
# add_number(1)
# print("после функции6", x, id(x))

# lst =[10,20,30]
# lst1 = (10,20,30)
# print(lst.__sizeof__())
# print(lst1.__sizeof__())

# a =(1,2,3,4,5)
# print(a,type(a))
# c = 1,2,3,4,5
# b = tuple("Hello")
# b = tuple(c)
# print(b, type(b))
# t =(2)
# print(type(t))
# tt = (2,)
# print(type(tt))
# a = (1,2,3,4,5)
# print(a)
# print(a[3])
# print(a[1:3])
# # a[3] = 55
# s = [int(input("=.")) for i in range(5)]
# print(s)

# s1 = tuple(int(input("=>"))for i in range(3))
# print(s1)

# from random import randint
# s2 = [randint(1,20) for _ in range(6)]
# s3 = tuple(randint(1,20)for _ in range(6))
# print(s2)
# print(s3)
# s4 = tuple(2** i for i in range(1,13))
# print(s4)
# t1 = tuple("hello")
# t2 = tuple("word")
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count("l"))
# print(t3.count("a"))
# print(t3.index('l', 3))
# if "w" in t3:
#     print(t3.index('w'))
# else:
#     print("Такого индесса нет")
#
# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             return tpl[tpl.index(el):tpl(el,tpl.index(el)+1)+1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
# print(slicer((1,2,3),8))
# print(slicer((1,8,2,3,8,8,8,2),8))
# print(slicer((1,2,8,3,1,2,3),8))

# def tuple_func(start, end):
#     return tuple(randint(start, end) for _ in range(10))
#
#
# tuple_1 = tuple_func(0, 5)
# tuple_2 = tuple_func(-5, 0)
# tuple_3 = tuple_1 + tuple_2
# count_0 = tuple_3.count(0)
#
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print('Count 0:', count_0)

# t = (10,"hello",[1,2,3], (4,5,6),['hello', 'word'])
# print(t, id(t))
# t[-1][0] = 'new'
# print(t,id(t))
# print(t[1][2])
# t[4].append('hi')
# print(t, id(t))
# t = (1,2,3)
# x,e,z = t
# print(x,e,z)
# def get_user():
#     name = "Tome"
#     age = 22
#     is_married = False
#     return name, age, is_married
# user = get_user()
# print(user)
# name1, age1, ismar=user
# print(user[0])
# print(user[1])
# print(name1,age1,ismar)
# name2, age2, ismar2=get_user()
# print(2, name2,age2, ismar2)
# t = (1,2,3)
# print(t)
# print(list(t))
# m = list(t)
# print(m)
# m.append(4)
# print(m)
# m = tuple(m)
# print(m)
# contrees = (
#     ('Gemaini', 80.2, (('Berlin', 3.326), ('Gamburg', 1.718))),
#     ('france', 75.2, (('Paris', 3.426), ('Marsek', 2.718)))
# )
# for contre in contrees:
#     print(contre)
#     contryName, contryPopulation, citis =contre
#     print("\n Country", contryName, 'nation', contryPopulation)
#     for city in citis:
#         cityName, cityPopylation = city
#         print(cityName, cityPopylation)
# Множество(set)
# s = {x*x for x in range(10)}
# print(s)
# numbers = [1, 2 , 3 , 5, 2,2,2, 6, 3, 9 ]
# num = {i for i in numbers if i%2==0}
# print(num)
# num = list(set(numbers))
# print(num)
# t ={"red",'green','blue'}
# print('green' not in t)

# s =['ab_1',"ac_2", "bc_1", "bc_2"]
# # a = {i for i in s if "a" not in i}
# a = {"A" + i[1:] if i[0] =='a' else "B" + i[1:] for i in s }
# print(a)
# a = {0,1,2,3}
# a.add(4)
# a.remove(2)
# a.discard(5)
# a.pop()
# print(a)
# a= {0,1,2,3}
# b = {4,3,2,1}
# c = a.union(b)
# c =a|b
# c=a&b
# c = a -b
# c=a^b
# print(c)
# s1 = "Hello"
# s2 = "How are yor"
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")
# s2 = "Python"
# s3 = 'Programming langues'
# s4 = set(s2) - set(s3)
# print(s4)
# frozeenset
# s = frozenset([1,2,3,4,5])
# print(s)
# print(type(s))
# словарь (dict)
# d1 = {'one': 'jone', 'two': 'jtwo'}
# d2 = dict(one="jone", two='jtwo')
# print(d1)
# print(d2)

# d = {0: 'text1', 'one': 45, (1, 2, 3): 'tuple', 42: [1, 2, 3], True: 1}
# print(d)
# d['one'] = 100
# print(d)
# d[42][1]=6
# print(d)
# d = {a: a*2 for a in  range(2, 7)}
# print(d)

# users = [
#     ['igor@gmail.com', "igor"],
#     ['irina@gmail.com', 'irina'],
#     ['anna@gmail.com','anna']
#
# ]
# d_user = dict(users)
# print(d_user)
# sers = (
#     ('igor@gmail.com', "igor"),
#     ('irina@gmail.com', 'irina'),
#     ('anna@gmail.com','anna')
#
# )
# for key in d_user:
#     print(d_user[key])

# a = {"one": 1, 'two':2,"three":3}
# # del a['two']
# print(a)
# key = 'two1'
# if key in a:
#     del a[key]
# print(a)
# try:
#     del a[key]
# except KeyError:
#     print("Элекмента с ключом", key,"нет в словоре")
# print(a)

# v = {'x1': 3, "x2": 7, "x3": 5, "x4": -1}
# res_v = 1
# for key in v:
#     res_v *= v[key]
# print(res_v)
# d= dict()
# d[1] = input("--->")
# d[2] = input("--->")
# d[3] = input("--->")
# d[4] = input("--->")
# print(d)
# dislike = int(input("Исключить:--->"))
# del d[dislike]
# print(d)

# dd = {i: input("--->") for i in range(1, 5)}
# print(dd)
# dislike1 = int(input("Исключить:--->"))
# del dd[dislike1]
# print(dd)
# a = {"one": 1, 'two':2,"three":3}
# print(len(a))

# goods = {
#     "1": ["Core -i3-4330", 9, 4500],
#     "2": ["Core -i5-4670", 3, 8550],
#     "3": ["AMD FX -6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core -i5-3450", 5, 6400],
# }
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1], "шт.", 'по ', goods[i][2], 'руб', sep=" ")
# while True:
#     n = input("N:->")
#     if n != "0":
#         m = int(input("Количество: -->"))
#         goods[n][1] = m
#
#
#     else:
#         break
# for i in goods:
#     print(i, ")", goods[i][0], "-", goods[i][1], 'шт.по ', goods[i][2], 'руб', sep=" ")

# a = {"one": 1, 'two': 2, "three": 3}
# print(a["two"])
# value = a.get('two')
# print(value)
# value1 = a.get('two1', 'Ключа нет')
# print(value1)
# print(a.keys())
# print(a.items())
# print(a.values())
# for i in a:
#     print(i)
# for i in a.keys():
#     print(i)
# for i in a.values():
#     print(i)
# for i in a.items():
#     print(i)
# for key, value3 in a.items():
#     print(key, "--->" ,value3)
# a.clear()
# print(a)
# a2 = {"one": 1, 'two': 2, "three": 3}
# a3 = a2.copy()
# print('a2',a2)
# print('a3', a3)
# a2['four']= 5
# a3['five']=4
# print('a2',a2)
# print('a3', a3)
# a5 = {"one": 1, 'two': 2, "three": 3}
# item = a5.pop("two")
# print(item)
# print(a5)
# item1 = a5.pop('two1',"Key is not")
# print(item1)
# item2 = a5.setdefault('four',5)
# print(item2)
# print(a5)
# item3 = a5.popitem()
# print(item3)
# print(a5
#       )
# a6 = {"one": 1, 'two': 2, "three": 3}
# a6.update({'four': 4, "five":5})
# print(a6)
# a6.update([('four',14), ('five',15)])
# print(a6)
# x = {'a':1, 'b':2}
# y = {'b':3, 'c':4}
# z = x.copy()
# z.update(y)
# print(z)
# z1 = x|y
# print(z1)
# z3 = {i: d[i] for d in [x, y] for i in d}
# print(z3)
# d = {'name': 'kelly', 'age': 25, 'salary':8000, 'city': 'New York'}
# new_d = dict()
# new_d['salary'] = d.pop('salary')
# new_d['name'] = d.pop('name')
# print(d)
# print(new_d)
# d['location'] = d.pop('city')
# print(d)
# a = {
#     'first':{
#         1: 'one',
#         2: 'two',
#         3:'three'
#     },
#     'second':{
#         4:'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t",y,': ', a[x][y], sep = " ")
#


# stud = {}
# n = int(input("Количество студентов: -->"))
# sr_ball = 0
# for i in range(n):
#     sname = int(str(i+1)+ 'й - студнет')
#     point = int(input("Балл -->"))
#     stud[sname] = point
#     sr_ball+=point
# print(stud)
# avr_ball = sr_ball/n
# print(round(avr_ball,2))
# for i in stud:
#     if stud[i] > avr_ball:
#         print(i)


# dict_one ={'name': 'Igor', 'last_name':'Doee', 'job':'consultant'}
# dict_two ={'name': 'Irina', 'last_name':'Smith', 'job':'Manadger'}
# for k, v in zip(dict_one.items(), dict_two.items()):
#     print(k, v)

# dict_one1 ={'name': 'Igor', 'last_name':'Doee', 'job':'consultant'}
# dict_two1 ={'name': 'Irina', 'last_name':'Smith', 'job':'Manadger'}
# for (k1, v1),(k2,v2) in zip(dict_one1.items(), dict_two1.items()):
#     print(k1, v1)
#     print(k2, v2)

# paris = [(1,'a'),(2,"b"),(3,'c'),(4,'d')]
# print(dict(paris))
# a, b = zip(*paris)
# print(a)
# print(b)
# letters =['a', 'b','c','d']
# numbers = [1, 2, 3,4]
# data = list(zip(letters,numbers))
# print(data)
# data.sort()
# print(data)
# data1= list(zip(numbers, letters))
# data1.sort()
# print(data1)
# data2 = dict(data1)
# print(data2)
# data3 = sorted(data2.items())
# print(data3)

# one = {'apple': 0.4, 'orange': 0.35, 'peper': 0.5}
# two = {'peper': 0.8, 'onion':0.55}
# print ({**two, **one})
# # for v,k in {**two,**one}.items():
#     print(k,'--->', v)

# data = [2,5,3,4,1,5]
# for i  in data:
#     print(i, end=" ")
# print()
# for i in range(6):
#     print(i, end=" ")
# colors= ['red', 'gren', 'blue']
# print()
# i = 1
# for color in colors:
#     print(i,")", color, sep=" ")
#     i+=1
# colors= ['red', 'gren', 'blue']
# for num, val in enumerate(colors, 1):
#     print(num,")", val,sep=" ")

# n = {i: i+1 for i in range(10,18)}
# print(n)
# for i, (j, v) in enumerate(n.items(), 100):
#     print(i,' : ', j," -->" , v, sep='')
# a = [1, 2, 3]
# b = [a, 4, 5 , 6, 7]
# c = a +b
# print(b)
# print(c)
# a1 = [1, 2, 3]
# b1 = [*a, 4, 5 , 6, 7]
# c1 = a1 +b1
# print(b1)
# print(c1)

# def func(*args):
#     res = 0
#     for i in args:
#         res+=i
#     return res
# print(func(2,3,4,5,6))
# print(func(2,4,7))
# print(func())
# def to_dict(*lst):
#     mir = {}
#     for i in lst:
#         mir[i]=i
#     return mir
# print(to_dict(1,2,3,4))
# print(to_dict('gray',(2,17),3.11, -4))
#
# def to_everg(*lst):
#     res=[]
#     sum1 = 0
#     j = 0
#     for i in lst:
#         sum1 +=i
#         j +=1
#     for i in lst:
#         if i < sum1/j:
#             res.append(i)
#     return res
# print(to_everg(2,5,6))


# def func (a, *args):
#     return a,args
# print(func(1))
# print(func(1,2, 2 ,9 , 10))

# def print_sqer(student, *cxo):
#     print("student Name", student)
#     for score in cxo:
#         print(score)
#
#
# print_sqer("Dgonotan",10,95,88,82,99)

# def func(**kwards):
#     return kwards
# print(func(a=1,b=2,c=3))
# print(func())
# print(func(d='python'))

# def intro(**data):
#     my_dict.update(data)
#     ...
# my_dict ={'one':'first'}
# intro(k1=22,k2=31, k3=11,k4=91)
# intro(name='Bob',age=31, weigh=68,eyes='green')
# print(my_dict)
# def func (a1, *args, b1=0,**kwargs):
#     return a1, args, b1, kwargs
# print(func("one",5,8,9,10,1, a=1, b=2,c=3, b1=589))

# Область видимости

# name = 'Tome'
# def hi():
#     global name
#     name = "Sev"
#     surname = 'Jonson'
#     print('Hello', name, surname)
# def byu():
#     print("Good buy", name)
# hi()
# byu()

# i = 5
# def func(arg=i):
#     print(arg)
# i = 6
# func()
# def add_five(a):
#     x=10
#
#     def add_two():
#
#         return a + x
#     return add_two()
# print(add_five(3))

# import builtins
# name = dir(builtins)
# for r in name:
#     print(r)

# a =[5,6,8,9,7]
# print(min(a))
# def func1():
#     a = 6
#     def func2(b):
#         a=4
#         print("a+b=", a + b)
#     print("a=",a)
#     func2(4)
# func1()
# x = 25

# def fn():
#     global t
#     a = 30
#     def innet():
#         nonlocal a
#         a = 35
#         print("non loca--->",a)
#     innet()
#     t = a
# fn()
# z = x+t
# print(z)
# x = 5
# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x->", x)
#
#     fn2()
#     print("fn1.x->", x)
#
#
# fn1()

# def outer(a1,b1,a2,b2):
#     a =0
#     b=0
#     def inner():
#         print(a)
#         a= a1+a2
#         b = b1+b1
#     inner()
#
# посмотреть позже
#
# def outer(n):
#     def inner(x):
#         return n +x
#     return inner
# add1 = outer(5)
# print(add1)
# print(add1(10))
# print(outer(7)(10))
# def func1():
#     a =1
#     b = 'line'
#     c = [1,2,3]
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a +1
#         b = b +"1"
#         return a,b,c
#     return func2
# func = func1()
# print(func())

# def func1(city):
#     s=0
#
#     def func2():
#         nonlocal s
#         s+=1
#         print(city, s)
#     return func2
#
# res = func1("Moscow")
# res()
# res()
# res2 = func1('Cochi')
# res2()
# res2()
#
# res()

# students = {
#     "Alise": 98,
#     "bod": 67,
#     "Crils": 85,
#     'david': 75,
#     'Ella': 35,
#     'cif': 69
# }
# def make_classifier(lower,upper):
#     def classify_student(exame):
#         return {k: v for k, v in exame.items() if lower <=v < upper}
#     return classify_student
# A = make_classifier(80,100)
# B = make_classifier(70,80)
# C = make_classifier(50,70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))


# Аннимная функция или лямда выражения

# print((lambda x, y: x+y)(1,2))
# print((lambda x, y: x+y)("a","b"))
# func = lambda x,y: x+y
#
# def summa(x,e):
#     return x+e
#
# print(summa(1,2))
# print(summa("a","b"))

# print((lambda x,e: x**2+e**2)(2,5))
#
# s = lambda a=1, b=2,c=3: a+b+c
# print(s())
# print(s(10,10,10))
# s1 = lambda *args:args
# print(s1(1,2,3,4))

# f = (lambda x:x*2,
#      lambda x:x*3,
#      lambda x:x*4
#      )
# for i in f:
#     print(i("abc_"))
# def inc(n):
#     return lambda x: x+n
# inc = (lambda n: (lambda x: x+n))
# print(inc(25)(-25))
# f = inc(42)
# print(f(1))
# print(f(5))

# inc = (lambda x: lambda y: lambda z: x+y+z)
# print(inc(2)(4)(6))
# d = {'a':10, 'b':12, 'c':4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i:i[1])
# print(lst)

# d = [
#     {"name": "Anton", "lastname": "birukov", 'rating': 9},
#     {"name": "Aleks", "lastname": "Bosdd", 'rating': 10},
#     {"name": "Fedor", "lastname": "sibrkd", 'rating': 4},
#     {"name": "Mike", "lastname": "semkiv", 'rating': 6},
# ]
#
# res = sorted(d, key=lambda item: item['lastname'])
# print(res)
# res1 = sorted(d, key=lambda item: item['rating'])
# res2 = sorted(d, key=lambda item: item['rating'], reverse=True)
# print(res1)
# print(res2)

# a = [(lambda x,y: x+y), (lambda x,y: x-y), (lambda x,y: x*y)]
# b = a[2](15,5)
# print(b)
# a={"one": lambda x: x-1, 'two': lambda x:x+3, 'tree': lambda x:x}
# b = {-10, 10,0, 25}
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['tree'](i))
# d = {
#     1: lambda: print('Понедельник 1'),
#     2: lambda: print('Понедельник 2'),
#     3: lambda: print('Понедельник 3'),
#     4: lambda: print('Понедельник 4'),
#     5: lambda: print('Понедельник 5'),
#     6: lambda: print('Понедельник 6'),
#     7: lambda: print('Понедельник 7')
# }
# d[4]()
# print((lambda a, b: a if a > b else b)(15, 13))
# print((lambda a, b, c: (a if a > c else c) if a > b else (b if b > c else c))(15, 28, 8))

# def mult(t):
#     return t*2
# lst = [1,8,12,-5,-10
#        ]
# lst = list( map(mult, lst))
# print(lst)

# areas = [3.5698,58.5698231,5.236871]
# print(list(map(round,areas)))
# print(list(map(round, areas, range(1,3))))

# st = ['a','b','c','d','e']
# num = [1,2,3,4,5]
# print(list(map(lambda x,y:(x,y),st,num)))
# l1 = [1,2,3]
# l2 = [4,5,6]
# print(list(map(lambda x,y:(x+ y),l1,l2)))
#
# print(dict(map(lambda x,y:(x,y),st,num)))

# t = ('abcd', 'acd','dddrdnn','ddi')
# print(tuple(filter(lambda s: len(s) ==3,t)))
# b = [66, 90,68,76,60,88,74,81,65]
# res = list(filter(lambda s: s>75, b))
# print(res)
# n = 10
# d = [ i for i in n random(0, 50)]

#

# 17/01/23 dekorator

# def hello():
#     return "Hello, I am func 'hello"
# def super_func(func):
#     print("Hello I am super _func")
#     print(func())
# super_func(hello)

# def hello():
#     return "Hello, I am func 'hello'"
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before ')
#         func()
#         print('Code after')
#     return func_wrapper
#
# def func_test():
#     print("Hello, I am func'func_test '")
# test = my_decorator(func_test)
# test()

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before ')
#         func()
#         print('Code after')
#     return func_wrapper
# @my_decorator
# def func_test():
#     print("Hello, I am func'func_test '")
# func_test()
# # test = my_decorator(func_test)
# # test()
# @my_decorator
# def bye():
#     print("Hello,  I am func 'bue'")
# bye()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn()+"<b>"
#     return wrap
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn()+"<i>"
#     return wrap
# @italic
# @bold
# @italic
# def hello():
#     return 'text'
# print(hello())

# def visov(fn):
#     count = 0
#     def chet():
#         nonlocal count
#         fn()
#         count+=1
#         print("Вызов функциии", count)
#
#     return chet
#
# @visov
# def hello():
#     print("Hello")
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1,arg2):
#         fn(arg1, arg2)
#     return wrap
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first,last)
#
#
# print_full_name("Irina","Vetrovs")

# def args_decorator(fn):
#     def wrap(*args,**kwargs):
#         print("Данные",args)
#         print(kwargs)
#         print("1)", args[0])
#         print('kwrgs', kwargs)
#         print('kwrgs', kwargs['study'])
#         fn(*args, **kwargs)
#     return wrap
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a,b,c,'изучают', study)
#
#
# print_full_name("Irina","Vetrovs",'katy', study= "JavaScript")
# print_full_name("Irina","Vetrovs",'katy2', )

# def decor(arags1, arags2):
#     def args_dec(fn):
#         def wrap(x,y):
#             print(arags1, x, "and", y, arags2, end="")
#             fn(x,y)
#         return wrap
#     return args_dec
#
# @decor("Cumma",'+')
# def summa(a,b):
#     print(a +b)
# summa(5, 2)

# dodilatm nachalo 2 pari

# @decor("Разность",'-')
# def sub(a,b):
#     print(a-b)
# sub(5,2)

# def typed(*args,**kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             print(args)
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('Некореектный ввод данных')
#             for k in kwargs:
#                 if type (f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Не корректный тип данных")
#             return fn(*f_args,**f_kwargs)
#
#         return wrap
#     return wrapper
# @typed(int,int,int)
# def typed_fn(x, y,z):
#     return x*y*z

# @typed(str,str,str)
# def typed_fn2(x, y,z):
#     return x + y + z
#
# @typed(str,str,int)
# def typed_fn3(x, y,z):
#     return x*y*z

#
# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end=' ')
#             func(*args)
#         return wrap
#         if tx is None:
#             return my_decorator
#         else:
#             return  my_decorator(tx)
#     return my_decorator
# @args_decorator
# def hello_words(text):
#     print(text)
# @args_decorator(decorator_text="Hello,")
# def hello_words2(text):
#     print(text)
#
# hello_words("Hi")
# hello_words2("word")
# print(bin(18))
# print(oct(18))
# print(hex(18))
# print(0b10010)
# print(0o22)
# print(0x12)
# print(0xFF0)
# q = "Pyt"
# w = 'hon'
# e = q +w
# print(e)
# print(e*3)
# print( e in "I am learn Python")
# print(e[5:0:-1])
# # e = 't'
# print(e)
# # e =e[:3] + 't'
# print(e)
# e =e[:3] + 't'+ e[4:]
# print(e)

# def chenge_letter(s, c_old, c_new):
#     i = 0
#     s2 = ' '
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = " Я изучаю Nython. Мне равиться Nython. Nython очень интересный язык программирования "
# str2 = chenge_letter((str1,"n",P'))

# #print(u'Привет')
# print("C:\\program\\file.txt")
# print(r"C:\program\file.txt")
# print(b'a1b2c3')
# print(b'a1b1c3'[1])
# print(b'\xff\xfe\xfd')
# print(b'\xff\xfe\xfd'[1])
# name = 'Дмитрий'
# age = 25
# print('Меня зовут', name, '.Мне', age, 'лет.', sep=' ')
# print('Меня зовут' +  name + '.Мне'+ str(age) + 'лет.')
# print(f' Меня зовут {name}. Мне {age} лет')
# from math import pi
#
# print(f'значение p:->{round(pi,2)}')
# print(f'значение p:->{pi:.2f}')
#
# x = 10
# y = 5
# print(f'{x=}\n{y=}')
# print(f'{x} x {y}/2 = {x*y/2}')
#
# a = 74
# print(f'{{{{{a}}}}}')
#
# dir_name = 'my_doc'
# file_name = "file.txt"
# print(fr'home\{dir_name}\{file_name}')
# print(f'home\\{dir_name}\\{file_name}')
# print(r'home\{dir_name}\{file_name}')

# s = """
# <div>
#
# """
#
#
#
# s1 = '''
# <div>
# '''
#
# print(s)

# def squer(n):
#     ''' Принимает число n, и возвращает квардрат числа n'''
#     return n**2
# print(squer(5))
# print(squer.__doc__)

import math as m

# def cylindr(r, h):
#     '''
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число , высота цилиндра
#     :return: положительное число площадь цилиндра
#     '''
#     return  2*m.pi*r*(r+h)
# print(cylindr(2,4))
# print(cylindr.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('k'))
# while True:
#     n = input('->')
#     if n !='-1':
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me"
# arr =[ord(x) for x in my_str]
# print('ASSCII code',arr)
# arr = [int(sum(arr)/len(arr))] + arr
# # arr.insert(0,df)
# # print(df)
# print(arr)
# arr+=[ x for x in [ord(x) for x in (input('-->' + " ")[:3])] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1])-1)
# arr.sort(reverse=True)
# print(arr)
git config global user.name "aran386"