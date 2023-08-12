class Person:
    def set_value(self, f_name, l_name, age, location):
        self.first_name = f_name
        self.l_name = l_name
        self.age = age
        self.location = location

    def print_value(self):
        print(self.first_name)
        print(self.l_name)
        print(self.age)
        print(self.location)


obj = Person()
obj.set_value("Amal", "n", 25, "thrissur")
obj.print_value()
obj.set_value("kiran", "m", 40, "ernakulam")
obj.print_value()
