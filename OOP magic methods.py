from accessify import private, protected

class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __new__(cls, *args):
        print('new' + str(cls))
        return super().__new__(cls)
 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
 
    def __getattribute__(self, item):
        if item == "_Point__x":
            raise ValueError("Private attribute")
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__delattr__: "+item)

    @protected
    def __str__(self) -> str:
        return str(self.__dict__)

    def __del__(self):
        print('delete')


class Coor(Point):
    def test(self):
        print(self.__str__())


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old
 
    def set_old(self, old):
        self.__old = old

    old = property(get_old, set_old)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name



pt1 = Point(3, 5)
pt1.b = 10
print(pt1.MIN_COORD)
print(pt1.a)
del pt1.b
print(pt1.__dict__)
print(dir(pt1))
# print(pt1.__str__())
dd = Coor(5, 8)
dd.test()
p = Person('Сергей', 20)
p.set_old(35)
print(p.get_old())
p.old = 41
print(p.old) 
p.__dict__['old'] = 'old in object p'
print(p.old, p.__dict__)
p.name = 'Вася'
print(p.name)
print(p.__dict__)
del p.name
print(p.__dict__)