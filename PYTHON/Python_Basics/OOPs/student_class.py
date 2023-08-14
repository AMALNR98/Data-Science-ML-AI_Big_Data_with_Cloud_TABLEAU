class Student:
    def keys(self, id ,f_name, l_name, age, collage_name):
        self.id = id
        self.first_name = f_name
        self.l_name = l_name
        self.age = age
        self.colllage_name = collage_name

    def print_value(self):
        print(self.id, self.first_name, self.l_name, self.age, self.colllage_name)


obj = Student()
obj.keys(100,"Amal", "n", 25, "sahrdaya")
obj.print_value()
obj.keys(101, "Akhil", "r", 25, "sahrdaya")
obj.print_value()
obj.keys(102, "john", "j", 24, "sahrdaya")
obj.print_value()
obj.keys(103, "robin", "babu", 25, "sahrdaya")
obj.print_value()
