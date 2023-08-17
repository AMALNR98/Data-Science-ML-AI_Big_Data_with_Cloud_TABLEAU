class A:
    def printa(self, num1):
        self.num1 = num1
        print("inside Class A", self.num1)

class B(A):
    def printb(self,num2):
        self.num2 = num2
        print("inside Class B",self.num2)

class C(B):
    def printc(self, num3):
        self.num_3 = num3
        print("Inside class c", self.num_3)


obj_1 = C()
obj_1.printc(10)
obj_1.printb(15)
obj_1.printa(30)
