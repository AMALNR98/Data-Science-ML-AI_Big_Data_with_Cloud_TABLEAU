# Class Person
# personal_data(id, fname, lname, age)

# Class Address
#   Information_data (district, country, phone-number)

# Class employee
#   Professional_data(Qualification, prof, experience, salary)

# Print -> id,fname,lname,age,district,phono,qualification,prof,salary,country


class Person:
    def personal_data(self, id, f_name, l_name, age):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.age = age

class Address:
    def information_data(self, district, country, phone_number):
        self.district = district
        self.country = country
        self.phone_number = phone_number

class Employee(Person, Address):
    def professional_data(self, qualification, prof, exp, salary):
        self.qualification = qualification
        self.prof = prof
        self.exp = exp
        self.salary = salary


        print(self.id,self.l_name,self.age,self.district,self.phone_number,self.qualification,self.prof, self.salary,self.country)


obj_1 = Employee()
obj_1.personal_data(1,"amal", "n r",25)
obj_1.information_data("nochiyil","thrissur","india")
obj_1.professional_data("b.tech", "data scientist", 2, 20000)
