# Have more than multiple parent classes for one child class
#   - More than one parent

class A:
    def printa(self, num1):
        self.num_1 = num1
        print("Inside class A", self.num_1)


class B:
    def printb(self, num2):
        self.num_2 = num2
        print("Inside class B", self.num_2)


class C(B, A):
    def printc(self, num3):
        self.num_3 = num3
        print("Inside class c", self.num_3)


obj_1 = C()
obj_1.printc(10)
obj_1.printb(15)
obj_1.printa(30)
