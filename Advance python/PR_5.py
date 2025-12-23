class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        Person.__init__(self, name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        Person.display(self)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Employee.__init__(self, name, age, emp_id, salary)
        self.department = department

    def display(self):
        Employee.display(self)
        print("Department:", self.department)


person = None
employee = None
manager = None


while True:
    print("\n--- Employee Management System ---")
    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        person = Person(name, age)
        print("Person created successfully.")

    elif choice == 2:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee ID: ")
        salary = int(input("Enter salary: "))
        employee = Employee(name, age, emp_id, salary)
        print("Employee created successfully.")

    elif choice == 3:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        emp_id = input("Enter employee ID: ")
        salary = int(input("Enter salary: "))
        dept = input("Enter department: ")
        manager = Manager(name, age, emp_id, salary, dept)
        print("Manager created successfully.")

    elif choice == 4:
        print("\nShow Details:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")
        ch = int(input("Enter choice: "))

        if ch == 1 and person is not None:
            person.display()
        elif ch == 2 and employee is not None:
            employee.display()
        elif ch == 3 and manager is not None:
            manager.display()
        else:
            print("No data found.")

    elif choice == 5:
        print("Exiting program.")
        break

    else:
        print("Invalid choice!")
