

a1 = []
a1pl = []
[ a1.append(int(input("=>"))) for i in range(int(input('Введите длинну спиcка: ')))]
print("Список: ",a1)
for i in a1:
    if i > 0:
      a1pl.append(i)
maxa1 = a1pl[0]
for j in a1pl:
    if j > maxa1:
        maxa1 = j
print("Новый список из положительных элементов: ",a1pl)
print("Наибольший элемент списка: ", maxa1 )



a2 = []
[ a2.append(int(input("=>"))) for i in range(int(input('Введите элементы списка n : ')))]
c2 = int(input("Введите индекс k : 0 <= k <= n   "))
print("k = ", c2)
d2 = int(input("Введите значение :"))
print("c = ",d2)
a2.insert(c2,d2)
print(a2)



a3 = []
for i in range(1, 10+1):
    a3.append(i**2)
print("Список квадратов =", a3)
