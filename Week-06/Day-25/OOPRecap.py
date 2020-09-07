
class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

        Employee.num_of_employees += 1

    @property
    def email(self):
        return self.first_name + '.' + self.last_name + "@company.com"

    @property
    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @fullname.deleter
    def fullname(self):
        print("Deleted Name!")
        self.first_name = None
        self.last_name = None

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, salary = emp_string.split('-')
        return cls(first, last, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.salary)

    def __str__(self):
        return "{} - {}".format(self.fullname, self.email)

    def __len__(self):
        return len(self.fullname)


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        self.employees = set(employees)
        # if employees is None:
        #     self.employees = []
        # else:
        #     self.employees = employees

    def add_emp(self, emp):
        self.employees.add(emp)

    def remove(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("B", "Z", 40000, "Python")
# dev_1.apply_raise()
# print(dev_1.salary)

mng_1 = Manager("Beimnet", "Z", 1000, [])
# print(mng_1.fullname())
mng_1.add_emp(dev_1)
# mng_1.print_emp()

emp = Employee("A", "Z", 100000)

# print(isinstance(mng_1, Employee))
# print(issubclass(Manager, Developer))
print(mng_1.__len__())


emp_1 = Employee("Beimnet", "Zewdu", 50000)
emp_1.raise_amount = 1.05
Employee.raise_amount = 1.06

# print(emp_1.fullname())
# print(emp_1.apply_raise())
# print(emp_1.salary)
# print(Employee.fullname(emp_1))

# print(emp_1.__dict__)

import datetime

# my_date = datetime.date(2019, 8, 23)
# print(Employee.is_workday(my_date))