class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id)
        self.salary = salary
        self.team_size = team_size

    def display_info(self):
        super().display_info()
        print(f"Position: Manager")
        print(f"Salary: ${self.salary}")
        print(f"Team Size: {self.team_size}")

    def conduct_meeting(self):
        print(f"{self.name} is conducting a team meeting.")

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Position: Engineer")
        print(f"Salary: ${self.salary}")
        print(f"Programming Language: {self.programming_language}")

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        super().display_info()
        print(f"Position: Salesperson")
        print(f"Salary: ${self.salary}")
        print(f"Sales Target: ${self.sales_target}")

    def make_sale(self):
        print(f"{self.name} made a sale and reached the sales target.")


manager = Manager(name="John Manager", employee_id=101, salary=80000, team_size=10)
manager.display_info()
manager.conduct_meeting()

engineer = Engineer(name="Alice Engineer", employee_id=201, salary=70000, programming_language="Python")
engineer.display_info()
engineer.write_code()

salesperson = Salesperson(name="Bob Salesperson", employee_id=301, salary=60000, sales_target=500000)
salesperson.display_info()
salesperson.make_sale()
