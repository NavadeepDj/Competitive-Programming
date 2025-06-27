[(Code for the Employee Probloem)](https://github.com/NavadeepDj/Competitive-Programming/blob/main/OOPS/basic_HierarchicalOOPS.py)

# Employee Management System - Python OOP Implementation

* A **base class** `Employee` with attributes:

  * `empName`, `empId`, and `department`
* Two **derived classes**:

  * `PermanentEmployee` with an additional `salary` attribute
  * `ContractEmployee` with an additional `contractDuration` attribute
* Methods to display employee details and proper constructors

---

## Python Classes Implemented

### 1. Base Class: `Employee`

```python
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
        print(f"Employee Name: {self.__empName}")
        print(f"Employee ID: {self.__empId}")
        print(f"Department: {self.department}")
```

### 2. Derived Class: `PermanentEmployee`

```python
class PermanentEmployee(Employee):
    def __init__(self, empName, empId, department, salary):
        super().__init__(empName, empId, department)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")
```

### 3. Derived Class: `ContractEmployee`

```python
class ContractEmployee(Employee):
    def __init__(self, empName, empId, department, contractDuration):
        super().__init__(empName, empId, department)
        self.__contractDuration = contractDuration

    def getContractDuration(self):
        return self.__contractDuration

    def display(self):
        super().display()
        print(f"Contract Duration: {self.__contractDuration} months")
```

---

## ❓ Doubts & Clarifications

### 🔸 Why use `self.__empName` and not access it directly in derived classes?

Python uses **name mangling** for attributes starting with `__`. For example, `__empName` becomes `_Employee__empName`.

* Inside `Employee`, `self.__empName` is valid
* Outside or in subclasses, use:

  * `self.getEmpName()` ✅ (Recommended)
  * or `self._Employee__empName` ❌ (Not recommended)

### 🔸 Why use getter methods?

Encapsulation best practices in OOP:

* Keeps class variables private
* Ensures safe and controlled access to data

### 🔸 Why does accessing `__empName` directly in subclass fail?

Because of name mangling. Subclass tries to find `self.__empName` → internally it looks for `_SubclassName__empName`, which does **not** exist.

### 🔸 Solution

Use getter methods defined in the base class to access private attributes.

```python
print(self.getEmpName())  # ✅ Safe
```

### 🔸 Can we override constructors like in Java?

Python doesn't support multiple constructors. So we use **default arguments**:

```python
class VehicleType:
    def __init__(self, type1=None, description=None):
        if type1 is None and description is None:
            print("Type: Car")
        else:
            self.type1 = type1
            self.description = description
            print(f"Type: {self.type1}, Desc: {self.description}")
```

---

## ✅ Summary of Concepts Used

| Concept              | Python Implementation |
| -------------------- | --------------------- |
| Class Inheritance    | `class A(B):`         |
| Private Variables    | `self.__var`          |
| Name Mangling        | `_ClassName__var`     |
| Constructor Chaining | `super().__init__()`  |
| Encapsulation        | Getter/Setter Methods |
| Method Overriding    | Redefine `display()`  |

---

## 👀 Output Samples

**Permanent Employee:**

```
Employee Name: Alice
Employee ID: EMP123
Department: IT
Salary: 75000.0
```

**Contract Employee:**

```
Employee Name: Bob
Employee ID: EMP456
Department: HR
Contract Duration: 12 months
```

---


## 🔗 References

* Python Docs on [Name Mangling](https://docs.python.org/3/tutorial/classes.html#private-variables)
