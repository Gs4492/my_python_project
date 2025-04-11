# employee.py

class Employee:
    def __init__(self, emp_id, name, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self._salary = salary 
        
    def show_info(self):
        print(f"{self.emp_id} | {self.name} | {self.role} | ₹{self._salary}")
        
    def update_role(self, new_role):
        self.role = new_role
        print(f"{self.name}'s role updated to {self.role}")
        
    def get_salary(self):
        return self._salary
    

class Developer(Employee):
    def __init__(self, emp_id, name, salary, language):
        super().__init__(emp_id, name, 'Developer', salary)
        self.language = language
        
    def show_info(self):
        super().show_info()
        print(f"Language: {self.language}")
        

class Manager(Employee):
    def __init__(self, emp_id, name, salary, team_size):
        super().__init__(emp_id, name, "Manager", salary)
        self.team_size = team_size

    def assign_task(self, task):
        print(f"{self.name} assigned task: {task}")


class Intern(Employee):
    def __init__(self, emp_id, name):
        super().__init__(emp_id, name, "Intern", 0)

    def request_extension(self):
        print(f"{self.name} requested internship extension.")
