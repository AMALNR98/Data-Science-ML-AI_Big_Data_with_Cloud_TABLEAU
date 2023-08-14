class Student:
    collage_name = 'Sahrdaya'

    def keys(self, id, f_name, l_name, age):
        self.id = id
        self.first_name = f_name
        self.l_name = l_name
        self.age = age

    def print_value(self):
        print(self.id, self.first_name, self.l_name, self.age, Student.collage_name)


obj = Student()
obj.keys(100, "Amal", "n", 25)
obj.print_value()
obj.keys(101, "Akhil", "r", 25)
obj.print_value()
obj.keys(102, "john", "j", 24)
obj.print_value()
obj.keys(103, "robin", "babu", 25)
obj.print_value()

# 2 types of variables
#   1. Instance variable or Dynamic variable    : in the above code snippet variables are defined inside "Method"
#   2. Static variable                          : static variables are declared inside "class name"
