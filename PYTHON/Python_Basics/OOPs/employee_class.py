class Employee:
    company_name = 'Microsoft'
    department = "AI"

    def keys(self, id, first_name, last_name, age, prof):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.prof = prof

    def print_value(self):
        print(self.id, self.first_name, self.last_name, self.age, Employee.department, Employee.company_name)


obj = Employee()
obj.keys(100, 'amal','n r', 25, 'senior strategist')
obj.print_value()
obj.keys(101, 'kiran','joby',25, 'developer')
obj.print_value()
obj.keys(100, 'abel','k p', 25, 'tester')
obj.print_value()
obj.keys(100, 'rijo','a k', 25, 'hr')
obj.print_value()