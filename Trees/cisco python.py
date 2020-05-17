"""def f():
    global a
     print(a)
     a = "hello"
     print(a)
 a = "world"
 f()
 print(a)"""

"""import functools
l=[1, 2, 3, 4, 5]
m=functools.reduce(lambda x, y:x if x>y else y, l)
print(m)"""

"""def foo(i, x=[]):
    x.append(i)
    return x
for i in range(3):
    print(foo(i))"""

"""class A:
    def __str__(self):
        return '1'
class B(A):
    def __init__(self):
        super().__init__()
class C(B):
    def __init__(self):
        super().__init__()
def main():
    obj1 = B()
    obj2 = A()
    obj3 = C()
    print(obj1, obj2,obj3)
main()"""




"""def f():
    global a
    print(a)
    a = "hello"
    print(a)
a = "world"
f()
print(a)"""

"""i = 1
while True:
    if i%3 == 0:
        break
    print(i)
 
    i += 1"""