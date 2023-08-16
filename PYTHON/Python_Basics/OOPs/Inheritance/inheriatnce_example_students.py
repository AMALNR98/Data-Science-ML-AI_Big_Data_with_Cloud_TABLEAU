# Student
# Method 1 ===> id, fname,lanme, age, loc
# Education
# Method 2 ===> sub_1, sub_2, sub_3
# Print id, fname, lanme, age, sub_1, sub_2, sub_3, Total_marks, location

class Student:
    def person_data(self, id, f_name, l_name, age, loc):
        self.id = id
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.loc = loc

class Education(Student):
    def marks(self, sub_1, sub_2, sub_3):
        self.sub_1 = sub_1
        self.sub_2 = sub_2
        self.sub_3 = sub_3
        self.total_marks = sub_1 + sub_2 +sub_3

        print(self.id, self.first_name,self.last_name,self.age,self.sub_1,self.sub_2,self.sub_3,self.total_marks,self.loc)

obj_2 = Education()
obj_2.person_data(1, "amal", "n r", 25, "Thrissur")
obj_2.marks(19,14,25)