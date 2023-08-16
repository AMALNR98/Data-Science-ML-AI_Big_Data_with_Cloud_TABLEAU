# Inheritance

class A:
    def printa(self, num1):
        self.num1 = num1
        print("Inside class A", self.num1)


class B(A):  # Here we're inheriting class A from class B
    def printb(self, num2):
        self.num2 = num2
        print("Inside class B", self.num2)


obj1 = A()
obj1.printa(10)

obj2 = B()
obj2.printb(10)
obj2.printa(10)  # Calling class A method form class B
