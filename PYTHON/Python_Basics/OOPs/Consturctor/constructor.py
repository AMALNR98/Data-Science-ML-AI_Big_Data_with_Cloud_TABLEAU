# constructor

# Class:
#   constructor(instance_variable)
# object = Class(values)

class Employee:
    def __int__(self, id, f_name, l_name, age):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

    def print_value(self):
        print(self.id, self.f_name, self.l_name, self.age)


employee_1 = Employee(100, 'vinay', 'k', 27)
employee_1.print_value()
