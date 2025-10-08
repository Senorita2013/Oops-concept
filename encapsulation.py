#activity 1
class myClass:

    __privatevar = 27

    def __privMeth(self):
        print("I'm inside class myClass")

    def hello(self):
        print("Private variable value:",myClass.__privatevar)

foo = myClass()
foo.hello()
foo.__privMeth

#activity 2
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling price:{}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()

#activity 3
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
    
p1 = Point(2,3)
print(p1)