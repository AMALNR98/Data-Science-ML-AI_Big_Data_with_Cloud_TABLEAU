# class : class name
class Person:  # try to use nouns, starting with capital letter is good
    # method : function
    def reading(self):  # self is instance keyword ---> instance variable
        print("reading text!")

    def printing(self):
        print("printing text!")


obj = Person()
obj.reading()
obj.printing()
