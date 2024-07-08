class Employee:
    def __init__(self, name, basic_salary, hra, da, cca):
        self.name = name
        self.basic_salary = basic_salary
        self.hra = hra
        self.da = da
        self.cca = cca

    def calculate_salary(self):
        salary = self.basic_salary + self.hra + self.da + self.cca
        return salary


employee1 = Employee("janu", 50000, 10000, 8000, 5000)
employee2 = Employee("kavya", 60000, 12000, 9000, 6000)
employee3 = Employee("harsha", 55000, 11000, 8500, 5500)


print(f"Salary of {employee1.name}: {employee1.calculate_salary()}")
print(f"Salary of {employee2.name}: {employee2.calculate_salary()}")
print(f"Salary of {employee3.name}: {employee3.calculate_salary()}")
