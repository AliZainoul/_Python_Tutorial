class Employee:
    def __init__(self, name: str, salary:float = 0.0):
        if salary < 0:
          raise ValueError("The salary cannot be negative")
        self._name=name
        self._salary=salary

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name : str) -> None:
        self._name = name
       
    def get_salary(self) -> float:
        return self._salary
    
    def set_salary(self, salary: float) -> None:
        if salary < 0:
          raise ValueError("The salary cannot be negative")
        self._salary = salary
    
    def display(self):
        return f"Employee : \n- name : {self._name} \n- Salary : {self._salary} Euros"

employee1= Employee(" Laya ", 3000)


print(employee1.display())