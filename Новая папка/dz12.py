
def func_comput(m):
    print("m->", m)
    def func_coc(c):
        print("c - >", c)
        return m*c
    return func_coc

a1 = int(input("Ввeдите аргумент  ->"))
res=func_comput(a1)
b1 = int(input("Введите заданное число->"))
print("res ->", res(b1))


print((lambda x,y,z: x*y*z)(2,5,5))

a3 = [
    {'name': 'Jenifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nicolos', 'final': 98},
]
res31 = sorted(a3, key=lambda bur: bur['name'])
res32 = sorted(a3, key=lambda bur: bur['final'], reverse=True)
print(res31)
print(res32)

a4 = [
    {'name': 'Jenifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nicolos', 'final': 98},
]
res41 = sorted(a4, key= lambda rup: rup['final'], reverse=True)
print(type(res41))
print(res41)
print(" Максимальная оценка", res41[0])
print( "Миниальная оценка",res41[-1])