a1 = ['red', 'green', 'blue']
b1 = ['#FF0000', "#008000", "000FF"]
c1 = {}
for i in range(len(a1)):
    c1.update({a1[i]: b1[i]})
    print(c1)

a2 = {i: i ** 3 for i in range(1, 10 + 1)}
print(a2)

a3 = {1: 10, 2: 20}
b3 = {3: 30, 4: 40}
c3 = {5: 50, 6: 60}
res3 = a3 | b3 | c3
print(res3)

a4 = {
    'emp1': {"name": "Jon", "salaru": 7500},
    'emp2': {"name": "Emma", "salaru": 8000},
    'emp3': {"name": "Brad", "salaru": 6500},
}
res4 = a4['emp3']['salaru']
res4 = 8500
a4['emp3']['salaru'] = 8500
print(res4)
print(a4['emp3'])

a5 = ['color', 'frut', 'pet']
b5 = ['blue', 'appel', 'dog']
c5 = dict(zip(a5, b5))
print(c5)

a6 = {}
srq = 0
b6  = int(input("Введите количество студентов: --> "))
for i in range(0,b6):
    c6 = input(str(i+1) + "- й студент ")
    ball = int(input("Балл ->"))
    a6[c6] = ball
for i in a6:
    srq +=a6[i]
d6 = srq/b6
print('Средний балл',round(d6), ' Студенты с баллом выше среднего:' )
print()
for i in a6:
    if a6[i] >d6:
        print(i, end=' ')