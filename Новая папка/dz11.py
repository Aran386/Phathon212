

def fn_sqw(a,b,c):
    def fn_sq(c,d):
        s = c*d
        return s
    s_s = fn_sq(a,b)*2 + fn_sq(a,c)*2 + fn_sq(b,c)*2
    return s_s
a1 = int(input("Введите ребро параллеприда а-->"))
b1 = int(input("Введите ребро параллеприда b-->"))
c1 = int(input("Введите ребро параллеприда c-->"))
print("Площадь параллепипеда ->", fn_sqw(a1,b1,c1))


s_s1 = 0
def fn_sqw(a,b,c):

    def fn_sq(c,d):
         s = c*d
         return s
    global s_s1
    s_s1 = fn_sq(a,b)*2 + fn_sq(a,c)*2 + fn_sq(b,c)*2
a2 = int(input("Введите ребро параллеприда а-->"))
b2 = int(input("Введите ребро параллеприда b-->"))
c2 = int(input("Введите ребро параллеприда c-->"))
fn_sqw(a2,b2,c2)
print("Площадь параллепипеда ->", s_s1)

def fn_sqw(a,b,c):
    s1 = 0
    s2 = 0
    s3 = 0

    def fn_sq(c,d,m):
         nonlocal s1, s2, s3
         s1 = c*d
         s2 = c*m
         s3 = d*m
    fn_sq(a,b,c)
    s_s = s1*2 + s2*2 + s3*2
    return s_s
a3 = int(input("Введите ребро параллеприда а-->"))
b3 = int(input("Введите ребро параллеприда b-->"))
c3 = int(input("Введите ребро параллеприда c-->"))

print("Площадь параллепипеда ->",fn_sqw(a3,b3,c3))