# main.py

from employee import Employee, Developer, Manager, Intern

employees = []

def add_employee():
    print("\n--- Add New Employee ---")
    emp_id = input("Enter ID: ")
    name = input("Enter Name: ")
    role = input("Enter Role (Developer/Manager/Intern): ")
    
    if role.lower() == "intern":
        emp = Intern(emp_id, name)
    else:
        salary = int(input("Enter Salary: "))
        if role.lower() == "developer":
            lang = input("Enter Programming Language: ")
            emp = Developer(emp_id, name, salary, lang)
        elif role.lower() == "manager":
            team_size = int(input("Enter Team Size: "))
            emp = Manager(emp_id, name, salary, team_size)
        else:
            emp = Employee(emp_id, name, role, salary)
        
    employees.append(emp)
    print(f"{name} added successfully!\n")
    
    
def show_all_employees():
    print("\n--- All Employees ---")
    for emp in employees:
        emp.show_info()
        print("-" * 30)
        
def update_employee_role():
    print("\n--- Update Role ---")
    emp_id = input("Enter Employee ID to update role: ")
    for emp in employees:
        if emp.emp_id == emp_id:
            new_role = input("Enter new role: ")
            emp.update_role(new_role)
            return
    print("Employee not found!")
    
def main_menu():
    while True:
        print("""
=== Employee Management System ===
1. Add Employee
2. Show All Employees
3. Update Role
4. Exit
""")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            show_all_employees()
        elif choice == '3':
            update_employee_role()
        elif choice == '4':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice. Try again!")
            
if __name__ == "__main__":
    main_menu()
