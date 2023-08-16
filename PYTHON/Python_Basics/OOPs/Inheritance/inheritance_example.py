# Person

# Personal data ==========> id, f_name, l_name, age, loc

# Employee data ==========> qualification, prof, dep, salary

# Print employees complete details ===> id, f_name, l_name, qualification, prof, dep, salary, loc


class Person:
    def person_data(self, id, f_name, l_name, age, loc):
        self.id = id
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.loc = loc


class Employee(Person):
    def employee_data(self, qualification, prof, dep, salary):
        self.qualifcation = qualification
        self.prof = prof
        self.dep = dep
        self.salary = salary

        print(self.first_name, self.last_name, self.age, self.qualifcation, self.prof, self.dep, self.salary)


# obj_1 = Person
# obj_1.person_data("1","amal", "n r", 25, "Thrissur")

obj_2 = Employee()
obj_2.person_data(1, "amal", "n r", 25, "Thrissur")
obj_2.employee_data("b.tech", "data scientist", "AI", 25000)
