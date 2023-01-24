import random

a1 = []
[ a1.append(int(input("=>"))) for i in range(int(input('Введите элементы спиcка n: ')))]
b1 = int(input("Введите число =>"))
print("ch = ", b1)
if b1 in a1:
    print("Число присутвует в элементах списка")
else:
    print('Числа нет в элементах списка')



a2 =[random.randint(1, 100) for _ in range(20)]
print(a2)
sum_a2 = 0
for i in a2:
    sum_a2+=i
print( "Summa :", sum_a2)

a3 = [random.randint(-100, 100) for _ in range(10)]
print(a3)
a3.sort(reverse=True)
print(a3)
for i in range(0,10):
    if a3[-1] < 0:
            a3.remove(a3[-1])
print(a3)

a4, b4 = 3, 4
pr = 1
c4 = [[random.randint(0, 4) for x in range(a4)]for y in range (b4)]
for i in c4:
    for z in i:
        print(z,end="\t\t")
        if z > 0:
            pr*=z

    print()
print("Произведение не нулевых элементов списка=> ", pr)