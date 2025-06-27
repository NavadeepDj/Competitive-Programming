class Employee:
    def __init__(self, empName, empId, department):
        self.__empName = empName
        self.__empId = empId
        self.department = department
    
    def getEmpName(self):
        return self.__empName
    def getEmpId(self):
        return self.__empId
    def display(self):
        print(f"Employee name {self.getEmpName()}\nEmployee Id: {self.getEmpId()}Employee Dept: \n{self.department}")
        
        
class PermanentEmployee(Employee):
    def __init__(self,empName, empId, department, salary):
        super().__init__(empName,empId, department )
        self.salary = salary
    
    def display(self):
        super().display()
        print(f"Salary: {self.salary}")
        
        
class ContractEmployee(Employee):
    def __init__(self, empName, empId, department, contractDuration):
        super().__init__(empName, empId, department)
        self.__contractDuration = contractDuration
    
    def getContractDuration(self):
        return self.__contractDuration
        
    def display(self):
        super().display()
        print(f"Contract Duration: {self.__contractDuration}")
        
        
class Main:
    print("Employee type: \n 1. PermanentEmployee \n 2. ContractEmployee ")
    type1 = int(input())
    name = input("Enter name: ")
    emp_id = input("Enter employee ID: ")
    dept = input("Enter department: ")

    if type1 == 1:
        salary = float(input())
        emp = PermanentEmployee(name, emp_id, dept, salary)
    elif type1 == 2:
        duration = int(input())
        emp = ContractEmployee(name, emp_id, dept, duration)
    else:
        print("Invalid choice.")
        exit()

    print("Employee Details:")
    emp.display()
