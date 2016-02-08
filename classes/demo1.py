__author__ = 'tripi'


class MyCat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print(MyCat.name, MyCat.color)

while True:
    try:
        i = input("any number >>>>>> : ")
        i = int(i)


        def math(number):
            MyCat.__init__(input("enter name of cat :"), input("and color :"))
            print(number, " = 1")


        def math1():
            print("wrong number")
            raise TypeError


        if i == 1:
            math(i)
        else:
            math1()

    except ValueError:
        print("---------------Value error--------------")
    except TypeError:
        print("---------------Type Error---------------")